#!/bin/bash

echo "== Top 10 online users: "
awk '{a[$1]++}END{for(i in a){if(a[i]>2)print a[i],i}}' user_data.log | sort -k1nr |head -10
echo ""

echo "== The percentage of inactive users in one day:"
all_user_count=`cat user_data.log |awk '{print $1}' | sort | uniq | wc -l`
#echo $all_user_count
# reference from classmate: inactive_user_count=`
# cat $file |awk '{print $1,$4}' |sort -k 1|uniq  |awk '{list[$1]++;}END{for (val in list) print val, list[val];}'| awk '$2==1 {print $1}'|wc -l`

inactive_users=`awk '{a[$4]++}END{for(i in a){if(a[i]>2)print a[i],i}}' user_data.log | sort -k1nr | cut -d" " -f1 |grep 288 |wc -l`
#echo $inactive_users

percentage=`echo "scale=3;$inactive_users/$all_user_count*100"|bc`
echo $percentage%

