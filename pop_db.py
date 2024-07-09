from web_flask import app, db
from web_flask.models import User, Verse, Quiz

""" print(Quiz.query.all())"""

with app.app_context(): 
    quizzes = [
        {"question": "God created the world in six days and rested on the seventh.", "answer": True, "reason": None},
        {"question": "Noah built the ark after a great flood destroyed the Earth.", "answer": False, "reason": "Noah built the ark before the flood."},
        {"question": "Moses received the Ten Commandments on Mount Sinai.", "answer": True, "reason": None},
        {"question": "The Israelites wandered in the desert for 30 years.", "answer": False, "reason": "The Israelites wandered in the desert for 40 years."},
        {"question": "King David wrote most of the Psalms.", "answer": True, "reason": None},
        {"question": "David was the first king of Israel.", "answer": False, "reason": "Saul was the first king of Israel."},
        {"question": "Isaiah was a prophet who foretold the coming of the Messiah.", "answer": True, "reason": None},
        {"question": "Elijah was taken up to heaven in a whirlwind.", "answer": True, "reason": None},
        {"question": "Jesus was born in Bethlehem.", "answer": True, "reason": None},
        {"question": "Jesus had twelve disciples.", "answer": True, "reason": None},
        {"question": "The Parable of the Good Samaritan teaches about loving your neighbor.", "answer": True, "reason": None},
        {"question": "The Parable of the Prodigal Son is found in the Old Testament.", "answer": False, "reason": "The Parable of the Prodigal Son is found in the New Testament."},
        {"question": "Jesus turned water into wine at the wedding in Cana.", "answer": True, "reason": None},
        {"question": "Jesus healed a man born blind by spitting on the ground and making mud.", "answer": True, "reason": None},
        {"question": "Peter was the apostle who denied Jesus three times.", "answer": True, "reason": None},
        {"question": "Paul wrote the Book of Revelation.", "answer": False, "reason": "John wrote the Book of Revelation."},
        {"question": "Esther became queen and saved the Jewish people.", "answer": True, "reason": None},
        {"question": "Ruth was the mother of King Solomon.", "answer": False, "reason": "Bathsheba was the mother of King Solomon."},
        {"question": "The Tower of Babel was built to reach heaven.", "answer": True, "reason": None},
        {"question": "Jonah was swallowed by a whale because he obeyed God's command.", "answer": False, "reason": "Jonah was swallowed by a whale because he disobeyed God's command."},
        {"question": "Solomon was known for his wisdom.", "answer": True, "reason": None},
        {"question": "The Book of Genesis is the first book in the New Testament.", "answer": False, "reason": "The Book of Genesis is the first book in the Old Testament."},
        {"question": "The Sermon on the Mount includes the Beatitudes.", "answer": True, "reason": None},
        {"question": "Lot's wife turned into a pillar of salt because she looked back at Sodom.", "answer": True, "reason": None},
        {"question": "The Book of Psalms is a collection of 150 hymns and prayers.", "answer": True, "reason": None},
        {"question": "Gideon led 300 men to victory with God's help.", "answer": True, "reason": None},
        {"question": "The Ark of the Covenant contained the original Ten Commandments.", "answer": True, "reason": None},
        {"question": "Joseph interpreted Pharaoh's dreams and saved Egypt from famine.", "answer": True, "reason": None},
        {"question": "Daniel was thrown into the lion's den because he refused to worship the king.", "answer": True, "reason": None},
        {"question": "Samson lost his strength when Delilah cut his hair.", "answer": True, "reason": None},
        {"question": "The Book of Proverbs is attributed to King David.", "answer": False, "reason": "The Book of Proverbs is attributed to King Solomon."},
        {"question": "Jesus fed 5000 people with five loaves of bread and two fish.", "answer": True, "reason": None},
        {"question": "Jesus was baptized by John the Baptist in the Jordan River.", "answer": True, "reason": None},
        {"question": "Moses parted the Red Sea to lead the Israelites out of Egypt.", "answer": True, "reason": None},
        {"question": "The Good Shepherd lays down his life for the sheep.", "answer": True, "reason": None},
        {"question": "The Book of Romans was written by Paul.", "answer": True, "reason": None},
        {"question": "The Bible mentions three wise men who visited Jesus at his birth.", "answer": False, "reason": "The Bible mentions wise men but does not specify the number."},
        {"question": "John the Apostle is traditionally believed to have written the Gospel of John.", "answer": True, "reason": None},
        {"question": "The city of Jericho's walls fell after the Israelites marched around it seven times.", "answer": True, "reason": None},
        {"question": "The Book of Esther never mentions the name of God.", "answer": True, "reason": None}
    ]
    for quiz in quizzes:
        db.session.add(Quiz(**quiz))

    db.session.commit()








