S = False
R = 'Threads'
Q = input
P = Exception
L = 'Token'
K = 'ID'
G = print
C = True
D = range

import re, random as A, requests as H
from threading import Thread as T
from colorama import Fore as I, Style as M
from cfonts import render as U, say

J = M.BRIGHT
N = M.RESET_ALL
E = J + I.GREEN
O = J + I.RED
F = J + I.WHITE
V = C
B = {K: None, L: None, R: 40}


class W:
    def __init__(D):
        D.ID = B[K]
        D.Token = B[L]
        D.Alive = C

    def check_username(E, username):
        A = username
        B = H.get(f"https://t.me/{A}")
        D = B.text
        if f'<meta property="twitter:title" content="Telegram: Contact @{A}">' in D:
            return C
        else:
            return S

    def check_fragment(D, username):
        A = H.get(f"https://fragment.com/username/{username}")
        B = A.text
        if 'Unavailable' in B:
            return C
        else:
            return S

    def generate(self):
        # Real, meaningful name parts
        meaningful_roots = [
            'tech', 'data', 'spark', 'zen', 'eth', 'core', 'code', 'bot', 'mind',
            'cloud', 'byte', 'crypt', 'sync', 'net', 'dev', 'form', 'loop', 'flux',
            'node', 'meta', 'nano', 'chain', 'shift', 'ink', 'base', 'dark', 'vis', 'glow'
        ]

        suffixes = [
            'ify', 'gen', 'ly', 'ic', 'er', 'ed', 'or', 'ist', 'ity', 'io', 'oid', 'ate', 'ium', 'ive'
        ]

        # Prebuilt brand-style custom names
        short_custom = [
            'lacquir', 'naking', 'ethize', 'vextor', 'quorix', 'syniq', 'luxor', 'naviq',
            'mirion', 'crypten', 'omnive', 'tekium', 'mindor', 'datrix', 'neuxis', 'inkred', 'fluxen'
        ]

        def generate_brandable():
            method = A.choice(['combine', 'custom'])

            if method == 'custom':
                return A.choice(short_custom)

            for _ in range(10):  # Try multiple combinations
                root = A.choice(meaningful_roots)
                suffix = A.choice(suffixes)
                name = root + suffix
                if 4 <= len(name) <= 7:
                    return name

            # Fallback if all combos are too long
            return A.choice(short_custom)

        return generate_brandable()

    def send_notification(A, username):
        D = 'rduser.txt'
        B = username
        try:
            C = f"[⚡️] Hit  -> Telegram\n[⚡️] User -> @{B}\n[⚡️] Dev -> @boloradhey\n"
            E = f"https://api.telegram.org/bot{A.Token}/sendMessage"
            F = {'chat_id': A.ID, 'text': C}
            H.post(E, data=F)
            open(D, 'a').write(C)
        except P as G:
            open(D, 'a').write(B + '\n')

    def main(B):
        while C:
            try:
                A = B.generate()
                if B.check_username(A) and B.check_fragment(A):
                    G(f"{E}Username {F}@{A} {E}Is Available ✅.{N}")
                    B.send_notification(A)
                else:
                    G(f"{O}Username {F}@{A} {O}Is Unavailable ❌.{N}")
            except P as D:
                G(D)


if V:
    X = U('{Radhey}', colors=['white', 'cyan'], align='center')
    Y = f"""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {X}
      Programmer : @boloradhey ┃ Channel: @visoid

   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    """
    G(Y)
    B[K] = str(Q(f"{F}Enter Your Telegram ID -> {E}").strip())
    B[L] = str(Q(f"{F}Enter Your Telegram Token -> {E}").strip())
    Z = int(B[R])
    a = W().main
    for b in D(Z):
        T(target=a).start()
