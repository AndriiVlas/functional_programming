updateAt :: Int -> a -> [a] -> [a]
updateAt index value list
    | index < 0 = list
    | otherwise = go index list
        where
            go _ [] = []
            go 0 (_:xs) = value : xs
            go i (x:xs) = x : go (i - 1) xs

data Person = Person { name :: String, age :: Int } deriving Show
myPerson :: Person
myPerson = Person "Andrii" 20
incrementAge :: Person -> Person
incrementAge person = person {age = age person + 1}

removeAt :: Int -> [a] -> [a]
removeAt index list
    | index < 0 = list
    | otherwise = go index list
        where
            go _ [] = []
            go 0 (_:xs) = xs
            go i (x:xs) = x : go (i - 1) xs