import cv2
import numpy as np

def morph_images(image1_path, image2_path, points1, points2, alpha):
    """
    Morphs two images based on corresponding control points.

    Args:
        image1_path (str): Path to the first image.
        image2_path (str): Path to the second image.
        points1 (list of tuples): List of (x, y) coordinates of control points in the first image.
        points2 (list of tuples): List of (x, y) coordinates of corresponding control points in the second image.
        alpha (float): Morphing parameter between 0 and 1.
                       0: Output is identical to image1.
                       1: Output is identical to image2.

    Returns:
        numpy.ndarray: The morphed image. Returns None if images have different sizes or invalid input.
    """
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    if img1 is None or img2 is None:
        print("Error: Could not open one or both images.")
        return None

    h1, w1, _ = img1.shape
    h2, w2, _ = img2.shape

    if (h1 != h2) or (w1 != w2):
        print("Error: Images must have the same dimensions for simple morphing.")
        return None

    if len(points1) != len(points2) or len(points1) < 3:
        print("Error: Must provide the same number of at least 3 corresponding control points.")
        return None

    num_points = len(points1)
    points1 = np.array(points1, dtype=np.float32)
    points2 = np.array(points2, dtype=np.float32)

    # Calculate intermediate points
    points_morphed = (1 - alpha) * points1 + alpha * points2

    # Create Delaunay triangulation on the morphed points
    rect = (0, 0, w1, h1)
    subdiv = cv2.Subdiv2D(rect)
    for p in points_morphed:
        subdiv.insert(p)

    triangleList = subdiv.getTriangleList()

    if len(triangleList) == 0:
        print("Error: Could not create Delaunay triangulation.")
        return None

    img_morphed = np.zeros_like(img1, dtype=np.float32)

    for t in triangleList:
        pt1 = (int(t[0]), int(t[1]))
        pt2 = (int(t[2]), int(t[3]))
        pt3 = (int(t[4]), int(t[5]))

        # Find corresponding triangles in the original images
        index1 = -1
        index2 = -1
        index_morphed = -1

        # Find the indices of the morphed triangle vertices in the morphed points array
        for i in range(num_points):
            if np.allclose(points_morphed[i], pt1, atol=1e-6):
                index_morphed_pt1 = i
            if np.allclose(points_morphed[i], pt2, atol=1e-6):
                index_morphed_pt2 = i
            if np.allclose(points_morphed[i], pt3, atol=1e-6):
                index_morphed_pt3 = i

        # Get the corresponding vertices in the original images
        if 'index_morphed_pt1' in locals() and 'index_morphed_pt2' in locals() and 'index_morphed_pt3' in locals():
            triangle1 = [tuple(points1[index_morphed_pt1].astype(int)),
                         tuple(points1[index_morphed_pt2].astype(int)),
                         tuple(points1[index_morphed_pt3].astype(int))]
            triangle2 = [tuple(points2[index_morphed_pt1].astype(int)),
                         tuple(points2[index_morphed_pt2].astype(int)),
                         tuple(points2[index_morphed_pt3].astype(int))]
            triangle_morphed = [pt1, pt2, pt3]

            # Get the bounding rectangles for each triangle
            rect1 = cv2.boundingRect(np.array(triangle1))
            rect2 = cv2.boundingRect(np.array(triangle2))
            rect_morphed = cv2.boundingRect(np.array(triangle_morphed))

            # Get the triangle points within the bounding rectangles
            tri1_cropped = [(p[0] - rect1[0], p[1] - rect1[1]) for p in triangle1]
            tri2_cropped = [(p[0] - rect2[0], p[1] - rect2[1]) for p in triangle2]
            tri_morphed_cropped = [(p[0] - rect_morphed[0], p[1] - rect_morphed[1]) for p in triangle_morphed]

            # Create masks
            mask_morphed = np.zeros((rect_morphed[3], rect_morphed[2]), dtype=np.float32)
            cv2.drawContours(mask_morphed, [np.array(tri_morphed_cropped, dtype=np.int32)], 0, 1, -1)

            # Warp the corresponding triangular regions
            img1_cropped = img1[rect1[1]:rect1[1] + rect1[3], rect1[0]:rect1[0] + rect1[2]]
            img2_cropped = img2[rect2[1]:rect2[1] + rect2[3], rect2[0]:rect2[0] + rect2[2]]

            warp_mat1 = cv2.getAffineTransform(np.float32(tri1_cropped), np.float32(tri_morphed_cropped))
            warp_mat2 = cv2.getAffineTransform(np.float32(tri2_cropped), np.float32(tri_morphed_cropped))

            warped_triangle1 = cv2.warpAffine(img1_cropped, warp_mat1, (rect_morphed[2], rect_morphed[3]), None, cv2.INTER_LINEAR, cv2.BORDER_REFLECT_101)
            warped_triangle2 = cv2.warpAffine(img2_cropped, warp_mat2, (rect_morphed[2], rect_morphed[3]), None, cv2.INTER_LINEAR, cv2.BORDER_REFLECT_101)

            # Blend the warped triangles
            blended_triangle = (1 - alpha) * warped_triangle1 + alpha * warped_triangle2

            # Copy the blended triangle to the output image
            img_morphed[rect_morphed[1]:rect_morphed[1] + rect_morphed[3], rect_morphed[0]:rect_morphed[0] + rect_morphed[2]] += blended_triangle * np.expand_dims(mask_morphed, axis=2)

    return np.clip(img_morphed, 0, 255).astype(np.uint8)

if __name__ == "__main__":
    # Example usage:
    image1_path = 'lake-6480788_1920.jpg'  # Replace with the path to your first image
    image2_path = 'lighthouse-2372461_1920.jpg'  # Replace with the path to your second image

    # Define corresponding control points (must be the same number)
    # You'll need to manually select these points on both images
    points1 = [(50, 50), (200, 50), (125, 150), (75, 250), (225, 250)]
    points2 = [(75, 75), (225, 75), (150, 175), (100, 275), (250, 275)]

    # Morphing parameter (0 to 1)
    alpha = 0.5

    # Perform image morphing
    morphed_image = morph_images(image1_path, image2_path, points1, points2, alpha)

    if morphed_image is not None:
        # Display the morphed image
        cv2.imshow("Morphed Image", morphed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save the morphed image (optional)
        cv2.imwrite("morphed_image.jpg", morphed_image)