e = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''


with open('./day5_seed_fertilizer/inputs.txt', 'r') as archivo:
    e = archivo.read()


seeds = e.split('\n\n')[0].split(': ')[1].split(' ')
seeds = list(map(int, seeds))
maps = e.split('\n\n')[1:]
maps = [m.split('\n')[1:] for m in maps]
seeds_new = []

print(maps)

location_min = float('inf')



while true:


while len(seeds) > 0:
    seed_prin = seeds.pop(0)
    seed_fin = seed_prin + seeds.pop(0)
    num = 0
    
    while seed_prin <= seed_fin:
        num = seed_prin
        
        for ms in maps:
            
            for m in ms:
                m = m.split(' ')
                m = list(map(int, m))
                
                
                if num >= m[1] and num < m[1]+m[2]:
                    num = (num - m[1]) + m[0]
                    
                    break
        
        if num < seed_min:
            seed_min = num
        
        seed_prin += 1




        

print(seed_min)


 
