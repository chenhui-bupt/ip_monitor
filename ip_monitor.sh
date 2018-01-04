# run ip_monitor.py every 30 mins
*/30 * * * * python ip_monitor.py >> logs/bk-run.log 2>&1 