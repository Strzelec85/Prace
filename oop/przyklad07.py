# Mamy dwie liczby:
#
# 69:       01000101
# 15:       00001111

# and-bitowe    (iloczyn logiczny)
# 69:       01000101
# 15:       00001111
#           00000101    tylko wspólne bity
#  5:
print( 69 & 15 )

# or-bitowe     (suma logiczna)
# 69:       01000101
# 15:       00001111
#           01001111    bity występujące w przynajmniej jednej z liczb
# 79:
print( 69 | 15 )

# xor-bitowe    (różnica symetryczna)
# 69:       01000101
# 15:       00001111
#           01001010    bity występujące w dokładnie jednej z liczb
# 74:
print( 69 ^ 15 )

# przesunięcie w prawo
# 69:       01000101
# >> 3      00001000...
# 8
print( 69 >> 3 )

# przesunięcie w lewo
# 69:       01000101
# << 1      10001010
# 138
print( 69 << 1 )

# przesunięcie w lewo i prawo jest tożsame z mnożeniem i dzieleniem przez potęgę 2
print( 69 << 1, 69 * 2 )
print( 69 << 2, 69 * 4 )
print( 69 << 3, 69 * 8 )
print( 69 << 4, 69 * 16 )

print( 69 >> 1, 69 // 2 )
print( 69 >> 2, 69 // 4 )
print( 69 >> 3, 69 // 8 )
print( 69 >> 4, 69 // 16 )



