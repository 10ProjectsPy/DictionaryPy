import mysql.connector
import difflib
from difflib import get_close_matches
def main():
    positive = ['yes', 'y']
    con = mysql.connector.connect(
        user = "ardit700_student",
        password = "ardit700_student",
        host  = "108.167.140.122",
        database = "ardit700_pm1database"
    )
    coursor = con.cursor()
    while True:
        word = input("Enter a word or type 'qq' to exit: ")
        if word == 'qq':
            return 0
        while True:
            querry = coursor.execute(f"SELECT Definition FROM Dictionary WHERE Expression LIKE '{word}'")
            result = coursor.fetchall()
            if result:
                for definition in result:
                    print(definition[0])
                break
            else: 
                querry = coursor.execute(f"SELECT Expression FROM Dictionary WHERE length(Expression) <= {len(word)+2} ")
                terms = coursor.fetchall()
                all_terms = []
                for term in terms:
                    all_terms.append(term[0])
                suggestion = get_close_matches(word,all_terms,n=1,cutoff=0.7)
                if not suggestion:
                    print(f"The word '{word}' was not found\nNo similar word found\nTry new entry")
                    break
                prompt = input(f"Did you mean {suggestion[0]} ?")
                if prompt.lower() in positive:
                    word=suggestion[0]
                else:
                    break
           
main()