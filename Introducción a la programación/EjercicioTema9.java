package Ejercicios;

public class EjercicioTema9 {
    public static void main(String[] args){
        Cliente cliente1 = new Cliente(22,"Lucas", "12345", "2468");
        System.out.println("Informacion Cliente 1");
        System.out.println("EDAD: "+ cliente1.edad);
        System.out.println("NOMBRE: "+ cliente1.nombre);
        System.out.println("Telefono: "+ cliente1.telefono);
        System.out.println("Credito: "+ cliente1.credito);

        Trabajador trabajador1 = new Trabajador(25,"Juan", "14567", 1000000);
        System.out.println("Informacion Trabajador 1");
        System.out.println("EDAD: "+ trabajador1.edad);
        System.out.println("NOMBRE: "+ trabajador1.nombre);
        System.out.println("Telefono: "+ trabajador1.telefono);
        System.out.println("Credito: "+ trabajador1.salario);
    }
}

class Persona{
    int edad;
    String nombre;
    String telefono;
}

class Cliente extends Persona{
    String credito;
    public Cliente(int edad, String nombre, String telefono, String credito) {
        this.edad = edad;
        this.nombre = nombre;
        this.telefono = telefono;
        this.credito = credito;
    }
}

class Trabajador extends Persona{
    int salario;
    public Trabajador(int edad, String nombre, String telefono, int salario) {
        this.edad = edad;
        this.nombre = nombre;
        this.telefono = telefono;
        this.salario = salario;
    }
}

