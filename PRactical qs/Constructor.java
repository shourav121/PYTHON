public class Constructor {
    private String name;
    private int age;
    public Constructor() {
        name = "Unknown";
        age = 0;
        System.out.println("Default constructor called.");
    }
    public Constructor(String name, int age) {
        this.name = name; // 'this' keyword refers to the instance variable
        this.age = age;
        System.out.println("Parameterized constructor called.");
    }
    public Constructor(Constructor other) {
        this.name = other.name;
        this.age = other.age;
        System.out.println("Copy Constructor Called.");
    }
    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
    public static void main(String[] args) {
        Constructor obj1 = new Constructor(); // Default constructor
        Constructor obj2 = new Constructor("salina", 53); // Parameterized constructor
        Constructor obj3 = new Constructor(obj2); //Copy Constructor
        System.out.println("\nObject 1:");
        obj1.display();
        System.out.println("\nObject 2:");
        obj2.display();
        System.out.println("\nObject 3:");
        obj3.display();
    }
}
