import random
import math

#generate_kromosom generating kromosom with real value between 0 and 1    
def generate_kromosom(size_krom):
    kromosom = [];
    j = int;
    for i in range(size_krom):
        j = random.uniform(0,1);
        kromosom.append(round(j,2));
    return kromosom

#generate_population according size population and then generate_kromosom
def generate_population(size_population):
    population = [];
    for i in range(size_population):
        population.append(generate_kromosom(10));

    return population

#sum_kromosom_x1 to get sum that are using in function
def sum_kromosom_x1(kromosom):
    panjang = len(kromosom);
    sum = 0;
    for i in range(panjang//2):
        sum = sum + kromosom[i];

    return sum
#sum_kromosom_x2 to get sum that are using in function
def sum_kromosom_x2(kromosom):
    panjang = len(kromosom)//2;
    sum = 0;
    length = len(kromosom);
    while(panjang < length):
        sum = sum + kromosom[panjang];
        panjang = panjang + 1;
    
    return sum 

#dekode_kromosom using real
def dekode_kromosom(kromosom):
   min_X1 = -1;
   min_X2 = -1;
   max_X1 = 2;
   max_X2 = 1;
   sum_kromosomX1 = sum_kromosom_x1(kromosom);
   sum_kromosomX2 = sum_kromosom_x2(kromosom);
   nilai_x1 = min_X1 + (((max_X1 - min_X1) / 5)* sum_kromosomX1);
   nilai_x2 = min_X2 + (((max_X2 - min_X1) / 5)* sum_kromosomX2);
   return [nilai_x1,nilai_x2]

#function cos(x1)*sin(x2) - x1/x2 square 2 + 1
def function(kromosom):
    function = ((math.cos(kromosom[0])*math.sin(kromosom[1])) - (kromosom[0]/(math.sqrt(kromosom[1] + 1))));
    return function

#fitness_value to fin minimum value using c to the power of -h
def fitness_value(kromosom):
    hasil = dekode_kromosom(kromosom);
    c = 2;
    value_fitness = c**-(function(hasil));
    return value_fitness

#collecting all fitness and using fitness_value
def countallfitness(population,size_population):
    fitness = [];
    for i in range(size_population):
        fitness.append(fitness_value(population[i]));
    return fitness

#parent selection using RouletteWheelSelection
def RouletteWheelSelection(fitness,size_population):
    hasil = [];
    total = 0;
    for i in range(size_population):
        total+=fitness[i];

    r = random.random();
    indv = 0;
    while (r>0):
        r -= fitness[indv]/total;
        indv = indv + 1;
    return indv-1

#crossover function using single point
def crossover(p_1, p_2, pc):
    n = random.random();
    if (pc > n):
        value = random.randint(0,9);
        panjang = len(p_1);
        while(value < panjang):
            temp = p_2[value];
            p_2[value] = p_1[value];
            p_1[value] = temp;
            value = value + 1;        
    return p_1, p_2

#mutasi function to checking and change chromosom
def mutasi(p_1,p_2, pm):
    panjang = len(p_1);
    for i in range(panjang):
        n = random.random();
        if (pm > n):
            p_1[i] = random.uniform(0,1);
            p_2[i] = random.uniform(0,1);
    return p_1,p_2

#elitsm function is mechanism to find best individual fitness
def elitsm(fitness):
    best = fitness.index(max(fitness));        
    return best

pc = 0.7; #ProbabilityCrossOver
pm = 0.01; #ProbabilityMutation
generation = 100; #TotalGeneration
size_population = 75; #TotalSizePopulation
i = 0;
j = 0;
pop = [];
populasi_baru = [];
populasi = [];

#SurvivorSelection using Generational Replacement
pop = generate_population(size_population);
while(i < generation):
    fitness = countallfitness(pop,size_population);
    terbaik = elitsm(fitness);
    populasi_baru.append(pop[terbaik]);
    while (j < size_population):
        par_1 = RouletteWheelSelection(fitness,size_population);
        par_2 = RouletteWheelSelection(fitness,size_population);
        if(par_2 == par_1):
            par_2 = RouletteWheelSelection(fitness,size_population);
        offspring = crossover(pop[par_1],pop[par_2],pc);
        offspring = mutasi(offspring[0],offspring[1],pm);
        j += 1;
    populasi = populasi_baru;
    i += 1
fitness = countallfitness(populasi,size_population);
best = elitsm(fitness);

#printing the output
print("Hasil Yang Diperoleh : ");
print("Best Kromosom :",populasi[best]);
print("Nilai X1 dan X2 hasil decode :",dekode_kromosom(populasi[best]));


        

