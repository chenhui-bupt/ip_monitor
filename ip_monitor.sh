# run ip_monitor.py every 30 mins
*/30 * * * * python ip_monitor.py >> logs/run.log 2>&1 

# delete run.log every month day 1, hour 0, min 10
# 10 0 1 * * rm -rf logs/run.log