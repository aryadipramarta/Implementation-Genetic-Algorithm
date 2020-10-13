import random
import math

#generatekromosom using real
def generate_population(size_population):
    population = [];
    for i in range(size_population):
        population.append(generate_kromosom(8));

    return population

def sum_kromosom_x1(kromosom):
    panjang = len(kromosom)
    sum = 0
    for i in range(panjang//2):
        sum = sum + kromosom[i];

    return sum

def sum_kromosom_x2(kromosom):
    panjang = len(kromosom)//2;
    sum = 0;
    length = len(kromosom);
    while(panjang < length):
        sum = sum + kromosom[panjang];
        panjang = panjang + 1;
    
    return sum 

def dekode_kromosom(kromosom):
   min_X1 = -1;
   min_X2 = -1;
   max_X1 = 2;
   max_X2 = 1;
   sum_kromosomX1 = sum_kromosom_x1(kromosom);
   sum_kromosomX2 = sum_kromosom_x2(kromosom);
   print('Kromosom X1 =',sum_kromosomX1);
   print('Kromosom X2 =',sum_kromosomX2);
   nilai_x1 = min_X1 + ((max_X1 - min_X1 / 4)* sum_kromosomX1);
   nilai_x2 = min_X2 + ((max_X2 - min_X1 / 4)* sum_kromosomX2);

   return [nilai_x1,nilai_x2]

def function(kromosom):
    function = ((math.cos(kromosom[0])*math.sin(kromosom[1])) - (kromosom[0]/(math.sqrt(kromosom[1] + 1))));
    return function

def fitness_value(kromosom):
    hasil = dekode_kromosom(kromosom);
    print(hasil);
    print(function(hasil));
    value_fitness = -1*(1/function(hasil));
    return value_fitness

def countallfitness(population,size_population):
    fitness = [];
    for i in range(size_population):
        fitness.append(fitness_value(population[i]));

    return fitness

def RouletteWheelSelection(fitness):
    total = 0;
    for 

def generate_kromosom(size_krom):
    kromosom = [];
    j = int;
    for i in range(size_krom):
        j = random.uniform(0,1);
        kromosom.append(round(j,2));
    print(fitness_value(kromosom));


generate_kromosom(8);


