#!/bin/bash

jobscript="task_array.sh"
echo "Name of job script" $jobscript

jobids=$(ls ${jobscript}.o* -1 | grep -o -P '(?<=.o).*(?=-)' | sort | uniq)

function enter_choice {
    read -p "Combine (y/n/d) d=dry-run? " choice
    case "$choice" in
      y|Y ) echo "yes";;
      n|N ) echo "no";;
      d|D ) echo "dry";;
      * ) echo "invalid";;
    esac
}

for jobid in $jobids; do

    echo
    echo "Files to combine:"
    # sort by the task array ID after the '-'
    files=$(ls ${jobscript}.o${jobid}-* | sort -t'-' -k2 -n)
    echo $files

    choice=$(enter_choice)
    combined=${jobscript}.o${jobid}
    if [[ $choice == "yes" ]] ; then
        echo cat $files ">" $combined
        echo rm $files
        # almost the same as 'cat' above but we put an extra row in between
        for f in $files; do (cat "${f}" | sed '/^Resources requested:$/q' | \
            head -n -2; echo) >> $combined; done
        rm $files
    elif [[ $choice == "dry" ]] ; then
        echo cat $files ">" ${jobscript}.o$jobid
        echo rm $files
    fi

done
