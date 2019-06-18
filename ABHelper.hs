module Main where
import Control.Monad.Trans.Class
import Control.Monad.Random
import Data.List
import System.Random

type Permutation = [Int]

readInt :: IO Int
readInt = fmap read $ getLine

perms :: Int -> [Permutation]
perms n = do go n [[]]
  where
    ns = [0..9]
    go 0 ps = ps
    go n ps = go (n - 1) [x : p | x <- ns, p <- ps , notElem x p]

guess :: (RandomGen g) => [Permutation] -> RandT g IO [Permutation]
guess xs
  | length xs <= 1 = return xs
  | otherwise = do
      g <- uniform xs
      (a, b) <- lift $ do
        putStrLn . concat $ map show g
        putStrLn "A?"
        a <- readInt
        putStrLn "B?"
        b <- readInt
        return (a, b)
      let allMark = mark xs g
      let allZipped = filter (\z -> snd z == (a, b)) $ zip xs allMark
      guess $ map fst allZipped

mark :: [Permutation] -> Permutation -> [(Int, Int)]
mark [] _ = []
mark (x : xs) p = (markA x p, markB x p - markA x p) : mark xs p
  where
    markA x p = sum $ zipWith (\x y -> if x == y then 1 else 0) x p
    markB x p = sum $ map (\x -> if x `elem` p then 1 else 0) x

main :: IO ()
main = do
  putStrLn "how many numbers in a permutation(1~9)"
  n <- readInt
  if (n < 0 || n > 9)
  then putStrLn "Well ..."
  else do
    g <- getStdGen
    evalRandT (guess (perms n) >>= lift . print . concat) g


