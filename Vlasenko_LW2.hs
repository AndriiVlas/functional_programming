safeHead :: [a] -> Maybe a
safeHead[] = Nothing
safeHead(x:_) = Just x

safeDiv :: (Eq a, Fractional a) => a -> a -> Maybe a
safeDiv _ 0 = Nothing
safeDiv x y = Just (x / y)

mkMultiplier :: Num a => a -> (a -> a)
mkMultiplier x = \y -> y * x
double = mkMultiplier 2
triple = mkMultiplier 3
quadruple = mkMultiplier 4
quintuple = mkMultiplier 5

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

myMap :: (a -> b) -> [a] -> [b]
myMap _ [] = []
myMap f (x:xs) = (f x) : myMap f xs

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f a = [x | x <- a, f x]

avg :: (Fractional a) => [a] -> Maybe a
avg [] = Nothing
avg xs = Just (sum xs / fromIntegral (length xs))

processList :: [Int] -> [Int]
processList a = take 3 [x * x | x <- a, odd x]

findIndex :: Eq a => a -> [a] -> Maybe Int
findIndex x = go 0
    where
        go _ [] = Nothing
        go i (y:ys)
            | x == y = Just i
            | otherwise = go (i + 1) ys

applyAll :: [a -> a] -> a -> a
applyAll [] x = x
applyAll (f:fs) x = applyAll fs (f x)


binarySearch :: Ord a => [a] -> a -> Maybe Int
binarySearch list target = go 0 (length list - 1)
  where
    go low high
        | low > high = Nothing
        | midVal == target = Just mid
        | midVal < target = go (mid + 1) high
        | otherwise = go low (mid - 1)
      where
        mid = low + (high - low) `div` 2
        midVal = list !! mid


quickSort :: Ord a => [a] -> [a]
quickSort [] = []
quickSort (x:xs) = quickSort [y | y <- xs, y < x] ++ (x : [m | m <- xs, m == x]) ++ quickSort [z | z <- xs, z > x]

type Peg = String
type Move = (Peg,Peg)
hanoi :: Int -> Peg -> Peg -> Peg -> [Move]
hanoi n a c b -- a - початок, c - кінець, b - допоміжний
    | n > 0 = hanoi (n - 1) a b c ++ [(a, c)] ++ hanoi (n - 1) b c a
    | n == 1 = [(a, c)]
    | otherwise = []

main :: IO()
main = do
    print (safeHead [1,2,3])
    print (safeDiv 5 2)
    print (double 3)
    print (mkMultiplier 2 3)
    print (applyTwice (*2) 5)
    print (myMap (*2) [1,2,3])
    print (myFilter (>3) [1..10])
    print (avg [1,2,3,4])
    print (processList [1..10])
    print (findIndex 3 [1..10])
    print (applyAll[negate,(*2)](-1))
    print (binarySearch [1..10] 7)
    print (quickSort [6,7,3,4,6,6,7,3])
    print (hanoi 2 "A" "C" "B")