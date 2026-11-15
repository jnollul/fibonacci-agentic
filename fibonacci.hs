{-# LANGUAGE BangPatterns #-}

module Main (main) where

import Data.List (foldl')
import System.Environment (getArgs, getProgName)
import System.Exit (ExitCode(ExitFailure), exitWith)
import System.IO (hPutStrLn, stderr)

main :: IO ()
main = do
    arguments <- getArgs
    case arguments of
        [rawIndex] ->
            case parseIndex rawIndex of
                Nothing -> failWith "Index must be an integer."
                Just index
                    | index < 0 -> failWith "Index must be non-negative."
                    | otherwise -> print (fibonacci index)
        _ -> do
            program <- getProgName
            failWith ("Usage: " ++ program ++ " <non-negative-integer>")

failWith :: String -> IO a
failWith message = do
    hPutStrLn stderr message
    exitWith (ExitFailure 2)

parseIndex :: String -> Maybe Integer
parseIndex raw =
    let (sign, digits) =
            case raw of
                '-':rest -> (-1, rest)
                '+':rest -> (1, rest)
                _ -> (1, raw)
     in if null digits || any (not . isAsciiDigit) digits
            then Nothing
            else Just (sign * foldl' addDigit 0 digits)
  where
    isAsciiDigit character = character >= '0' && character <= '9'
    addDigit value digit =
        value * 10 + toInteger (fromEnum digit - fromEnum '0')

fibonacci :: Integer -> Integer
fibonacci index = go index 0 1
  where
    go 0 !previous _ = previous
    go !remaining !previous !current =
        go (remaining - 1) current (previous + current)
