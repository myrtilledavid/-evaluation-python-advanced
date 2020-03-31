from codec import TreeBuilder, Codec

text = "a dead dad ceded a bad babe a beaded abaca bed"

builder = TreeBuilder(text)
binary_tree = builder.tree()


# on passe l'arbre binaire à un encodeur/décodeur
codec = Codec(binary_tree)
# qui permet d'encoder
encoded = codec.encode(text)
# et de décoder
decoded = codec.decode(encoded)
# si cette assertion est fausse il y a un gros problème avec le code

# on affiche le résultat
print(f"{text}\n{decoded}")
if decoded != text:
    print("OOPS")