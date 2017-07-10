iptables -t nat -A PREROUTING -p tcp --dport 25 -j REDIRECT --to-ports 2500
iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-ports 2200
iptables -t nat -A PREROUTING -p tcp --dport 21 -j REDIRECT --to-ports 2100
iptables -t nat -A PREROUTING -p tcp --dport 23 -j REDIRECT --to-ports 2300
