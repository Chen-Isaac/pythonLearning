import random

adj = open("adj.txt","r")
pick_adj = random.choice(adj.readlines()).strip()
adj.close

n = open("n.txt","r")
pick_n = random.choice(n.readlines()).strip()
n.close

verb = open("verb.txt","r")
pick_verb = random.choice(verb.readlines()).strip()
verb.close

adv = open("adv.txt","r")
pick_adv = random.choice(adv.readlines()).strip()
adv.close

print "The %s %s %s %s." %(pick_adj, pick_n, pick_verb, pick_adv)