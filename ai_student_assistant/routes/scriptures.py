from flask import Blueprint, render_template, redirect, url_for
import random


scriptures = Blueprint("scriptures", __name__)


verses = [

    {
        "text": "I can do all things through Christ who strengthens me.",
        "ref": "Philippians 4:13"
    },

    {
        "text": "Be still, and know that I am God.",
        "ref": "Psalm 46:10"
    },

    {
        "text": "Trust in the Lord with all your heart and lean not on your own understanding.",
        "ref": "Proverbs 3:5"
    },

    {
        "text": "The Lord is my shepherd; I shall not want.",
        "ref": "Psalm 23:1"
    },

    {
        "text": "God has not given us a spirit of fear, but of power, love and a sound mind.",
        "ref": "2 Timothy 1:7"
    },

    {
        "text": "Commit your work to the Lord, and your plans will be established.",
        "ref": "Proverbs 16:3"
    },

    {
        "text": "Be strong and courageous. Do not be afraid, for the Lord your God is with you wherever you go.",
        "ref": "Joshua 1:9"
    },

    {
        "text": "Let your light shine before others, that they may see your good deeds.",
        "ref": "Matthew 5:16"
    },

    {
        "text": "The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
        "ref": "Psalm 34:18"
    },

    {
        "text": "Cast all your anxiety on Him because He cares for you.",
        "ref": "1 Peter 5:7"
    },

    {
        "text": "Those who hope in the Lord will renew their strength. They will soar on wings like eagles.",
        "ref": "Isaiah 40:31"
    },

    {
        "text": "The Lord will fight for you; you need only to be still.",
        "ref": "Exodus 14:14"
    },

    {
        "text": "Seek first the kingdom of God and His righteousness.",
        "ref": "Matthew 6:33"
    },

    {
        "text": "My grace is sufficient for you, for My power is made perfect in weakness.",
        "ref": "2 Corinthians 12:9"
    },

    {
        "text": "The joy of the Lord is your strength.",
        "ref": "Nehemiah 8:10"
    },

    {
        "text": "Whatever you do, work at it with all your heart, as working for the Lord.",
        "ref": "Colossians 3:23"
    },

    {
        "text": "Do not worry about tomorrow, for tomorrow will worry about itself.",
        "ref": "Matthew 6:34"
    },

    {
        "text": "Your word is a lamp for my feet and a light on my path.",
        "ref": "Psalm 119:105"
    },

    {
        "text": "We walk by faith, not by sight.",
        "ref": "2 Corinthians 5:7"
    },

    {
        "text": "The battle belongs to the Lord.",
        "ref": "1 Samuel 17:47"
    }

]



def generate_reflection():

    return (
        "Take a moment to reflect on this message. "
        "Let it guide your mindset, your studies and your daily choices."
    )



@scriptures.route("/scriptures")
def scriptures_page():

    verse = random.choice(verses)

    reflection = generate_reflection()


    return render_template(
        "scriptures.html",
        verse=verse,
        reflection=reflection
    )



@scriptures.route("/new-verse")
def new_verse():

    return redirect(
        url_for("scriptures.scriptures_page")
    )