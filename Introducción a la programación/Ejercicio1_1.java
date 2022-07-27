public class Ejercicio1_1 {

    public static void main(String[] args) {
        Coche miCoche = new Coche();
        miCoche.incrementoPuertas();
        System.out.println(miCoche.puertas);
    }

}

class Coche{
    public int puertas = 0;

    public void incrementoPuertas(){
        this.puertas++;
    }
}
