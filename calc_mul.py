#!/usr/bin/python3

import re
                
def calc(A,B):
        if type(A) is int and type(B) is int:   #intに制限することで小数と文字列を除外
                ai=str(A)
                bi=str(B)
                p = re.compile('\d+(\.\d+)?')
                if p.match(ai) or p.match(bi):
                        a=float(ai)
                        b=float(bi)
                        if 0<a and a < 100 and 0 < b and b<1000:        #aとbそれぞれに0と1000の間であるかの判定を設け、aとbの直接の比較をなくした
                                valid=True
                        else:
                                valid=False
                else:
                        valid=False
                        
                if valid:
                        ans=a*b
                        return ans
                else:
                        return -1
        
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
