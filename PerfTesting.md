# Tests de Performance

## Test avec les Aggregate
```
Sensors: 100k
Measures: 50M
```

### Test 1
Je récupère un capteur depuis sensors avec 50 mesures (au hasard) sans INDEX
```
=> 89754ms
```

### Test 2
Je récupère un capteur depuis sensors avec 50 mesures (au hasard) avec INDEX
```
=> 1ms
```

### Test 3
Je récupère 50 mesures depuis mesures en filtrant sur 1 capteur avec INDEX
```
=> la requête tombe en timeout
```

### Test 3 (idem test 3, léger changement de requête)
Je récupère 50 mesures depuis mesures en filtrant sur 1 capteur avec INDEX
```
=> la requête tombe en timeout
```

### Test 4
Je récupère 500 mesures depuis mesures en filtrant sur 1 capteur avec INDEX
```
=> 89ms
```

## Conclusion
! filtrer le plus tôt possible ( match )
! ne pas utiliser les lookup/unwind avec un match après si la relation n'est pas filtrée en amont avant le lookup
