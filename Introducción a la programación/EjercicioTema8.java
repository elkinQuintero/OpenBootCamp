package Ejercicios;

public class EjercicioTema8 {

    public static void main(String[] args){
        Persona1 persona1 = new Persona1();
        persona1.setEdad(23);
        persona1.setNombre("Lucas");
        persona1.setTelefono("12345");
        System.out.println("EDAD: "+ persona1.getEdad());
        System.out.println("NOMBRE: "+ persona1.getNombre());
        System.out.println("Telefono: "+ persona1.getTelefono());
    }
}

class Persona1{
    private int edad;
    private String nombre;
    private String telefono;

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
}
