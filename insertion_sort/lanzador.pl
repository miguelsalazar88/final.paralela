#!/usr/bin/perl

=begin comment
Fecha: 17 de Noviembre de 2022
Autor: Miguel Salazar di Colloredo
Proyecto: Tercer Parcial, Computación Paralela y Distribuida
Tema: Comparación de rendimiento: Python vs Cython
=cut

@benchmarks=("main.py");
@cargas = ("1","1000","2500","5000","7500","10000","12500","15000","17500","20000");
$n = 30;

$path = "/home/miguel/Desktop/computacion_paralela/final/insertion_sort/";
$ejecutable = "/home/miguel/Desktop/computacion_paralela/final/insertion_sort/main.py";

foreach $exes (@benchmarks){
    foreach $carga (@cargas){
        
        $file = "soluciones/".$exes."-size".$carga.".csv\n";
        system("echo Cython,Python >> $file");
        printf("$path$exes$file");
        for ($i=0; $i<$n; $i++){
            system("python3 $ejecutable $carga >> $file");
        }
    }
}