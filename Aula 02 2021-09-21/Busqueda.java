
/**
 * @author Diego Gustavo Montana Neyra
*/

public class Busqueda {
	
	/* Ejercicio 01
	 * Realiza la búsqueda de un elemento  en un arreglo
	 * Comprueba posición por posición hasta encontrarlo
	 */
	public static boolean sequencialSearch(int[] arr, int x){
	    for (int i = 0; i < arr.length; i++) {
	        if(arr[i] == x)
	            return true;
	    }
	    return false;
	}
	
	/* Ejercicio 02
	 * Genera un arreglo decreciente desde el valor ingresado hasta el número 1
	 */
	public static int[] genArrayDecrec(int n) {
		int arreglo[] = new int[n];
		for (int i = 0; i < arreglo.length; i++) {
			arreglo[i] = n;
			n--;
		}
		return arreglo;
	}
	
	
	/*Ejercicio 03
	 * Medir el tiempo de ejecucion de la función sequencialSearch
	 * Se ingresa como parámetro el tamaño del arreglo y el valor buscado
	 */
	public static double timeSequencial(int tamArr, int valor) {
		double tiempo;
		int [] arreglo = genArrayDecrec(tamArr);
		//medir tiempo
		double inicio = System.nanoTime();
		sequencialSearch(arreglo, valor);
		double fin = System.nanoTime();
		tiempo = (double)(fin - inicio)/1000000;
		return tiempo;
	}
	
	
	/* Ejercicio 04
	 * Genera un arreglo que guarda los tiempos de ejecucion para el algoritmo sequencial sort
	 * Los valores van de 10000 en 10000
	 * Recibe como parametro el tamaño del arreglo y el valor a buscar
	 */
	public static double[] timeArraySequencial(int n, int valor) {
		int tamArr = 10000;
		double [] arrayTime = new double [n];
		for (int i = 0; i < n; i++) {
			arrayTime[i] = timeSequencial(tamArr,valor);
			tamArr += 10000;
		}
		return arrayTime;
	}
	
	/*Ejercicio 05
	 * Ordena los elementos de un arreglo
	 */
	public static void insertionSort(int [] arr) {
		for (int j = 1; j < arr.length; j++) {
			int key = arr[j];
			int i = j - 1;
			while(i >= 0 && arr[i] > key) {
				arr[i + 1]= arr[i];
				i--;
			}
			arr[i + 1] = key;
 		}
	}
	
	/* Ejercicio 06
	 * Genera un arreglo que guarda los tiempos de ejecucion para el algoritmo insertion sort
	 * Los valores van de 100 en 100
	 * Recibe como parametro el tamaño del arreglo
	 * Se utilizaron 3 funciones
	 */
	//genera un arreglo con numeros random de tamaño n
	public static int[] genArrayRandom(int n) {
		int arreglo[] = new int[n];
		int numero = 0;
		for (int i = 0; i < n; i++) {
			numero = (int)(Math.random()*n);
			arreglo[i] = numero;
		}
		return arreglo;
	}
	//mide el tiempo de ejecucion del algoritmo insertion sort
	public static double timeInsertion(int tamArr) {
		double tiempo;
		int [] arreglo = genArrayRandom(tamArr);
		//medir tiempo
		double inicio = System.nanoTime();
		insertionSort(arreglo);
		double fin = System.nanoTime();
		tiempo = (double)(fin - inicio)/1000000;
		return tiempo;
	}
	//mide tiempos para el algoritmo insertion sort y los guarda en un arreglo
	//recibe como parametro el numero de elementos a evaluar
	public static double[] timeArrayInsert(int n) {
		int tamArr = 100;
		double [] arrayTime = new double [n];
		for (int i = 0; i < n; i++) {
			arrayTime[i] = timeInsertion(tamArr);
			tamArr += 100;
		}
		return arrayTime;
	}
	
	
	//Algoritmos para imprimir arreglos
	public static void impArreglo(int [] arr) {
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + ", ");
		}
		System.out.println();
	}
	public static void impArrDouble(double [] arr) {
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + ", ");
		}
		System.out.println();
	}
	
	
	
	
	public static void main(String[] args) {
		
		//Ejercicio 01 ejemplo
		System.out.println("Ejercicio 1:");
		int [] arreglo01 = {4,8,9,14,23,1,7,24,21};
		System.out.println(sequencialSearch(arreglo01, 21));
		System.out.println();
		
		//Ejercicio 02 ejemplo
		System.out.println("Ejercicio 2:");
		int [] arreglo02 = genArrayDecrec(20);
		impArreglo(arreglo02);
		System.out.println();
		
		//Ejercicio 03 ejemplo
		System.out.println("Ejercicio 3:");
		System.out.println(timeSequencial(50000,15));
		System.out.println();
		
		//Ejercicio 04 ejemplo
		System.out.println("Ejercicio 4:");
		impArrDouble(timeArraySequencial(200,1));
		System.out.println();
		
		
		//Ejercicio 05
		System.out.println("Ejercicio 5:");
		int [] arreglo03 = {5, 2, 4, 6, 1, 3, 14, 8};
		insertionSort(arreglo03);
		impArreglo(arreglo03);
		System.out.println();
		
		//Ejercicio 06
		System.out.println("Ejercicio 6:");
		impArrDouble(timeArrayInsert(150));
		System.out.println();
		
		
	}

}
