public class Ejercicio4_5 {

    public static void main(String[] args) {
        var estacion="Otoño";
        switch (estacion){
            case "Primavera":
                System.out.println("Es "+estacion);
                break;
            case "Verano":
                System.out.println("Es "+estacion);
                break;
            case "Otoño":
                System.out.println("Es "+estacion);
                break;
            case "Invierno":
                System.out.println("Es "+estacion);
                break;
            default:
                System.out.println("La estación "+estacion+" no existe");
        }
    }
}
