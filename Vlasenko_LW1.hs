doubleEven :: [Int] -> [Int]
doubleEven list = map (\x -> if even x then x * 2 else x) list

sumOdd :: [Int] -> Int
sumOdd [] = 0
sumOdd (x:xs) =
    if odd x then x + sumOdd xs
    else sumOdd xs

absList :: [Int] -> [Int]
absList absNumbers = map abs absNumbers

myLength :: [a] -> Int
myLength [] = 0
myLength (_:xs) = 1 + myLength xs

myReverse :: [a] -> [a]
myReverse [] = []
myReverse (x:xs) = myReverse xs ++ [x]

myMaximum :: Ord a => [a] -> a
myMaximum [x] = x
myMaximum (x:xs) = max x (myMaximum xs)

pyth :: [(Int, Int, Int)]
pyth = [(a, b, c) | a <- [1..20], b <- [a..20], c <- [1..20], c * c == a * a + b * b]

fib :: Int -> Int
fib n
    | n == 0 = 0
    | n == 1 = 1
    | otherwise = fib (n - 1)  + fib (n-2)