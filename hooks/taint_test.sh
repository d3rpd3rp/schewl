#!/bin/bash

sudo insmod hookme_exp.ko

echo "Inserting hookme now..."

sleep 2

echo "<more> command open of secret2.txt as $(id -u -n)"
more secret2.txt
sleep 1
echo "<more> command open of secret2.txt as $(sudo id -u -n)"
sudo more secret2.txt
sleep 1
echo "<cp> command open of secret2.txt to secret3.txt as $(id -u -n)"
cp secret2.txt secret3.txt
sleep 1
echo "<more> command open of secret3.txt as $(id -u -n)"
more secret3.txt
sleep 1
echo "<more> command open of secret2.txt as $(sudo id -u -n)"
sudo more secret3.txt
sleep 1


echo "Removing hookme now..."

sudo rmmod hookme_exp
