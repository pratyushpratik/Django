declare -i count=0
while true
do
    now=`date`
    git add .
    git commit -m "$now"
    git push origin master
    echo "git pushed : $count : $now"
    ((count++))
    sleep 3600
done
