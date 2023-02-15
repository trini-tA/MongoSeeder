# MongoSeeder 

Exemple de Seeder pour mongodb en Python

## Todo
* Mesurer le temps d'insertion

## Quelques commandes Docker
```
docker exec -it mongoseeder_mongodb /bin/bash
```
```
mongodump --archive --db bulk_example > bulk_dump.dump
```
```
docker exec mongoseeder_mongodb_1 sh -c 'exec mongodump --db bulk_dump --gzip --archive' > dump_`date "+%Y-%m-%d"`.gz
```

## Oh!
Extrait de https://blog.seboss666.info/2015/02/un-exemple-du-mauvais-usage-de-mongodb/
```
Quand vous dupliquez des données critiques (beurk), ou utilisez des références et opérez des jointures dans le code de votre application(double beurk), quand vous avez des liens entre les documents, vous avez surestimé MongoDB. Quand les gars de MongoDB disent « documents », de bien des manières, ils signifient des choses que l’on peut imprimer sur un bout de papier et tenir du bout des doigts. Un document peut avoir une structure interne –entêtes, sous-entêtes, paragraphes, pieds de pages– mais ils ne contiennent pas de liens vers d’autres documents. C’est un morceau indépendant de données semi-structurées.
Si vos données ressemblent à ça, vous avez des documents. Bravo ! C’est une bonne raison d’utiliser MongoDB. Mais s’il y a une raison d’avoir des liens entre les documents, alors vous n’avez pas de document. MongoDB n’est pas la bonne solution pour vous. Ce n’est certainement pas la bonne solution pour des données sociales, où les liens entres documents sont l’information la plus critique du système.
```
