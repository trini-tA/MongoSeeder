# Depuis sensors, avec 50 measures
```
[
   {
     $match: {
       _id: ObjectId("63eca35881446fc9ce5d6ffd"),
     },
 },
  {
    $lookup: {
      from: "measures",
      localField: "_id",
      foreignField: "sensor",
      as: "measures",
    },
  },
  {
    $unwind: {
      path: "$measures",
      //includeArrayIndex: "string",
      preserveNullAndEmptyArrays: true,
    },
  },
  {
    $sort: {
      timestamp: 1,
    },
  },
  {
    $limit: 50,
  },
]
```

# Depuis measures, timeout
```
[
  {
    $lookup: {
      from: "sensors",
      localField: "sensor",
      foreignField: "_id",
      as: "sensor",
    },
  },
  {
    $unwind: {
      path: "$sensor",
      //includeArrayIndex: "string",
      preserveNullAndEmptyArrays: true,
    },
  },
  {
    $match: {
      "sensor._id": ObjectId(
        "63eca35881446fc9ce5d6ffd"
      ),
    },
  },
  {
    $sort: {
      timestamp: 1,
    },
  },
  {
    $limit: 50,
  },
]
```

# Depuis measures, timeout
```
[
  {
    $lookup: {
      from: "sensors",
      localField: "sensor",
      foreignField: "_id",
      as: "sensor",
    },
  },
  {
    $match: {
      "sensor._id": ObjectId(
        "63eca35881446fc9ce5d6ffd"
      ),
    },
  },
  {
    $unwind: {
      path: "$sensor",
      //includeArrayIndex: "string",
      preserveNullAndEmptyArrays: true,
    },
  },
  {
    $sort: {
      timestamp: 1,
    },
  },
  {
    $limit: 50,
  },
]
```
