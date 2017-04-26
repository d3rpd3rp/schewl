#!/bin/bash

src_file=/media/sf_6813/assignment08/hookme_exp/hookme_exp_clean.c
dest_dir=/home/seed/Documents/assignment08/hookme_exp/
dest_file=/home/seed/Documents/assignment08/hookme_exp/hookme_exp_clean.c
d=$(diff $src_file $dest_file) 

if [ $(echo $d | wc -w) -gt 1 ]
 then
  echo "Differences in src and dest: "
  diff $src_file $dest_file
  rsync -av --progress $src_file $dest_dir
  sleep 1

  echo "File updated."
  echo $(date -r $dest_file)

  exit 1;
fi

echo "No difference in files."
