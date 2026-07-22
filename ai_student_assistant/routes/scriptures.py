from flask import Blueprint, render_template, request
import random

scriptures = Blueprint("scriptures", __name__)

ANCHIE_THOUGHTS = {

"wisdom": {

"thought":
"University life comes with many decisions. Ask God for wisdom and take your next step with confidence.",

"step":
"Spend 15 minutes reviewing something you have been avoiding."

},


"study": {

"thought":
"Learning takes patience. Small consistent efforts today create big results tomorrow.",

"step":
"Choose one topic and focus on understanding it deeply."

},


"peace": {

"thought":
"Stress can make everything feel bigger than it is. Give your worries to God and focus on what you can do today.",

"step":
"Take a short break, pray and return to your work with a clear mind."

},


"discipline": {

"thought":
"Your future is built through the small choices you make every day.",

"step":
"Create a simple study plan for your next session."

},


"hope": {

"thought":
"Hard seasons do not last forever. Keep moving forward with faith.",

"step":
"Write down one thing you are grateful for today."

}

}

VERSE_LIBRARY = {
"wisdom": [

{
"text":"The fear of the Lord is the beginning of wisdom, and knowledge of the Holy One is understanding.",
"ref":"Proverbs 9:10",
"reflection":"True wisdom begins by seeking God first."
},

{
"text":"Trust in the Lord with all your heart and lean not on your own understanding.",
"ref":"Proverbs 3:5",
"reflection":"God's guidance is greater than our limited perspective."
},

{
"text":"If any of you lacks wisdom, you should ask God, who gives generously to all without finding fault.",
"ref":"James 1:5",
"reflection":"God invites us to seek His wisdom in every situation."
},

{
"text":"The wise store up knowledge, but the mouth of a fool invites ruin.",
"ref":"Proverbs 10:14",
"reflection":"Learning and growing in knowledge requires humility."
},

{
"text":"Walk with the wise and become wise, for a companion of fools suffers harm.",
"ref":"Proverbs 13:20",
"reflection":"The people around us influence our growth."
},

{
"text":"A wise person is hungry for knowledge, while the fool feeds on trash.",
"ref":"Proverbs 15:14",
"reflection":"Choose information and influences that help you grow."
},

{
"text":"Do not forsake wisdom, and she will protect you; love her, and she will watch over you.",
"ref":"Proverbs 4:6",
"reflection":"Wisdom is a lifelong companion."
},

{
"text":"Teach us to number our days, that we may gain a heart of wisdom.",
"ref":"Psalm 90:12",
"reflection":"Time is valuable. Use it intentionally."
},

{
"text":"The beginning of wisdom is this: Get wisdom. Though it cost all you have, get understanding.",
"ref":"Proverbs 4:7",
"reflection":"Pursuing wisdom is always worth the effort."
},

{
"text":"Plans fail for lack of counsel, but with many advisers they succeed.",
"ref":"Proverbs 15:22",
"reflection":"Seeking guidance can help us make better decisions."
},

{
"text":"Blessed is the one who finds wisdom, the one who gains understanding.",
"ref":"Proverbs 3:13",
"reflection":"Wisdom brings lasting value."
},

{
"text":"The mouth of the righteous utters wisdom, and their tongues speak what is just.",
"ref":"Psalm 37:30",
"reflection":"Wisdom shapes both thoughts and words."
},

{
"text":"How much better to get wisdom than gold, to get insight rather than silver.",
"ref":"Proverbs 16:16",
"reflection":"Character and wisdom are more valuable than possessions."
},

{
"text":"Let the wise listen and add to their learning, and let the discerning get guidance.",
"ref":"Proverbs 1:5",
"reflection":"Growth requires a willingness to keep learning."
},

{
"text":"The wise in heart are called discerning, and gracious words promote instruction.",
"ref":"Proverbs 16:21",
"reflection":"Wisdom is reflected through humility and kindness."
}

],




"study": [

{
"text":"Whatever you do, work at it with all your heart, as working for the Lord.",
"ref":"Colossians 3:23",
"reflection":"Your studies can be an act of worship when done with excellence."
},

{
"text":"Commit to the Lord whatever you do, and He will establish your plans.",
"ref":"Proverbs 16:3",
"reflection":"Invite God into your academic journey."
},

{
"text":"Do you see someone skilled in their work? They will serve before kings.",
"ref":"Proverbs 22:29",
"reflection":"Developing your skills creates opportunities."
},

{
"text":"Lazy hands make for poverty, but diligent hands bring wealth.",
"ref":"Proverbs 10:4",
"reflection":"Consistency and effort produce growth."
},

{
"text":"I can do all things through Christ who strengthens me.",
"ref":"Philippians 4:13",
"reflection":"God provides strength for challenges."
},

{
"text":"Whatever your hand finds to do, do it with all your might.",
"ref":"Ecclesiastes 9:10",
"reflection":"Give your best effort with what is in front of you."
},

{
"text":"She sets about her work vigorously; her arms are strong for her tasks.",
"ref":"Proverbs 31:17",
"reflection":"Strength grows through commitment and discipline."
},

{
"text":"The plans of the diligent lead surely to abundance.",
"ref":"Proverbs 21:5",
"reflection":"Small consistent actions create progress."
},

{
"text":"Those who sow with tears will reap with songs of joy.",
"ref":"Psalm 126:5",
"reflection":"Hard seasons of learning can produce beautiful results."
},

{
"text":"Let perseverance finish its work so that you may be mature and complete.",
"ref":"James 1:4",
"reflection":"Growth requires patience."
},

{
"text":"Do not despise these small beginnings.",
"ref":"Zechariah 4:10",
"reflection":"Every great achievement starts somewhere."
},

{
"text":"The diligent will rule, but the lazy will be put to forced labor.",
"ref":"Proverbs 12:24",
"reflection":"Discipline creates freedom."
},

{
"text":"Teach me knowledge and good judgment, for I trust your commands.",
"ref":"Psalm 119:66",
"reflection":"Ask God for understanding as you learn."
},

{
"text":"A wise son brings joy to his father, but a foolish son brings grief to his mother.",
"ref":"Proverbs 10:1",
"reflection":"Our choices affect more than ourselves."
},

{
"text":"Apply your heart to instruction and your ears to words of knowledge.",
"ref":"Proverbs 23:12",
"reflection":"Learning requires attention and humility."
}

],

"peace": [

{
"text":"Peace I leave with you; my peace I give you. I do not give to you as the world gives.",
"ref":"John 14:27",
"reflection":"God offers a peace that remains even when circumstances are uncertain."
},

{
"text":"Cast all your anxiety on Him because He cares for you.",
"ref":"1 Peter 5:7",
"reflection":"You do not have to carry every burden alone."
},

{
"text":"The Lord gives strength to His people; the Lord blesses His people with peace.",
"ref":"Psalm 29:11",
"reflection":"God provides strength and calm in difficult seasons."
},

{
"text":"You will keep in perfect peace those whose minds are steadfast, because they trust in You.",
"ref":"Isaiah 26:3",
"reflection":"Peace grows when our focus remains on God."
},

{
"text":"Do not be anxious about anything, but in every situation, by prayer and petition, present your requests to God.",
"ref":"Philippians 4:6",
"reflection":"Prayer transforms worry into trust."
},

{
"text":"And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
"ref":"Philippians 4:7",
"reflection":"God's peace protects us beyond what we can explain."
},

{
"text":"When I am afraid, I put my trust in You.",
"ref":"Psalm 56:3",
"reflection":"Fear loses power when we place our trust in God."
},

{
"text":"The Lord is my shepherd, I lack nothing.",
"ref":"Psalm 23:1",
"reflection":"God cares for every need and walks with us."
},

{
"text":"Be still, and know that I am God.",
"ref":"Psalm 46:10",
"reflection":"Sometimes we need to stop striving and remember who God is."
},

{
"text":"The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
"ref":"Psalm 34:18",
"reflection":"God is near during painful seasons."
},

{
"text":"You will go out in joy and be led forth in peace.",
"ref":"Isaiah 55:12",
"reflection":"God desires to guide us into joy and peace."
},

{
"text":"May the Lord of peace Himself give you peace at all times and in every way.",
"ref":"2 Thessalonians 3:16",
"reflection":"God's peace is available in every season."
},

{
"text":"The mind governed by the Spirit is life and peace.",
"ref":"Romans 8:6",
"reflection":"What we focus on shapes our inner world."
},

{
"text":"In repentance and rest is your salvation, in quietness and trust is your strength.",
"ref":"Isaiah 30:15",
"reflection":"Resting in God brings renewed strength."
},

{
"text":"You will seek me and find me when you seek me with all your heart.",
"ref":"Jeremiah 29:13",
"reflection":"God invites us into a deeper relationship with Him."
}

],



"discipline": [

{
"text":"No discipline seems pleasant at the time, but painful. Later on, however, it produces a harvest of righteousness and peace.",
"ref":"Hebrews 12:11",
"reflection":"Growth often requires patience and commitment."
},

{
"text":"Whoever can be trusted with very little can also be trusted with much.",
"ref":"Luke 16:10",
"reflection":"Small acts of responsibility build character."
},

{
"text":"A little sleep, a little slumber, a little folding of the hands to rest, and poverty will come on you like a thief.",
"ref":"Proverbs 6:10-11",
"reflection":"Small habits can create big consequences."
},

{
"text":"The soul of the lazy craves and gets nothing, while the soul of the diligent is richly supplied.",
"ref":"Proverbs 13:4",
"reflection":"Desire alone is not enough; action matters."
},

{
"text":"Do not be deceived: God cannot be mocked. A man reaps what he sows.",
"ref":"Galatians 6:7",
"reflection":"Our daily choices shape our future."
},

{
"text":"Run in such a way as to take the prize.",
"ref":"1 Corinthians 9:24",
"reflection":"Pursue your goals with purpose and determination."
},

{
"text":"Let us not become weary in doing good, for at the proper time we will reap a harvest if we do not give up.",
"ref":"Galatians 6:9",
"reflection":"Consistency matters even when results are slow."
},

{
"text":"Whatever you do, do it all for the glory of God.",
"ref":"1 Corinthians 10:31",
"reflection":"Excellence can be a way of honoring God."
},

{
"text":"Work hard and become a leader; be lazy and become a slave.",
"ref":"Proverbs 12:24",
"reflection":"Discipline creates opportunities."
},

{
"text":"The plans of the diligent lead to profit as surely as haste leads to poverty.",
"ref":"Proverbs 21:5",
"reflection":"Careful effort produces lasting results."
},

{
"text":"A sluggard's appetite is never filled, but the desires of the diligent are fully satisfied.",
"ref":"Proverbs 13:4",
"reflection":"Discipline helps turn goals into reality."
},

{
"text":"Train yourself to be godly.",
"ref":"1 Timothy 4:7",
"reflection":"Spiritual growth requires intentional practice."
},

{
"text":"Make every effort to add to your faith goodness; and to goodness, knowledge.",
"ref":"2 Peter 1:5",
"reflection":"Growth happens through intentional development."
},

{
"text":"Be very careful, then, how you live, not as unwise but as wise.",
"ref":"Ephesians 5:15",
"reflection":"Live with purpose and awareness."
},

{
"text":"Teach us to number our days, that we may gain a heart of wisdom.",
"ref":"Psalm 90:12",
"reflection":"Time is a gift that should be used wisely."
}

],

"strength": [

{
"text":"I can do all things through Christ who strengthens me.",
"ref":"Philippians 4:13",
"reflection":"Your strength comes from God, not just your own ability."
},

{
"text":"Be strong and courageous. Do not be afraid or terrified because of them, for the Lord your God goes with you.",
"ref":"Deuteronomy 31:6",
"reflection":"God's presence gives courage when facing challenges."
},

{
"text":"The Lord is my strength and my shield; my heart trusts in Him, and He helps me.",
"ref":"Psalm 28:7",
"reflection":"Trusting God gives strength when you feel weak."
},

{
"text":"Those who hope in the Lord will renew their strength. They will soar on wings like eagles.",
"ref":"Isaiah 40:31",
"reflection":"Waiting on God brings renewed energy and endurance."
},

{
"text":"God is our refuge and strength, an ever-present help in trouble.",
"ref":"Psalm 46:1",
"reflection":"God remains our safe place during difficult moments."
},

{
"text":"The Lord is my light and my salvation; whom shall I fear?",
"ref":"Psalm 27:1",
"reflection":"Fear becomes smaller when we remember who walks with us."
},

{
"text":"Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.",
"ref":"Joshua 1:9",
"reflection":"God's presence gives confidence for every new season."
},

{
"text":"My grace is sufficient for you, for My power is made perfect in weakness.",
"ref":"2 Corinthians 12:9",
"reflection":"God can work through our weaknesses."
},

{
"text":"The Lord gives strength to the weary and increases the power of the weak.",
"ref":"Isaiah 40:29",
"reflection":"God meets us when our own strength runs out."
},

{
"text":"The righteous person may have many troubles, but the Lord delivers him from them all.",
"ref":"Psalm 34:19",
"reflection":"Challenges are real, but God remains faithful."
},

{
"text":"Wait for the Lord; be strong and take heart and wait for the Lord.",
"ref":"Psalm 27:14",
"reflection":"Patience and faith grow together."
},

{
"text":"The joy of the Lord is your strength.",
"ref":"Nehemiah 8:10",
"reflection":"True strength comes from the joy found in God."
},

{
"text":"The Lord will fight for you; you need only to be still.",
"ref":"Exodus 14:14",
"reflection":"Some battles are won through trusting God."
},

{
"text":"When you pass through the waters, I will be with you; and when you pass through the rivers, they will not sweep over you.",
"ref":"Isaiah 43:2",
"reflection":"God promises His presence through difficult seasons."
},

{
"text":"The Lord makes firm the steps of the one who delights in Him.",
"ref":"Psalm 37:23",
"reflection":"God guides those who seek Him."
},

{
"text":"Do not fear, for I am with you; do not be dismayed, for I am your God.",
"ref":"Isaiah 41:10",
"reflection":"God's presence replaces fear with confidence."
},

{
"text":"The name of the Lord is a fortified tower; the righteous run to it and are safe.",
"ref":"Proverbs 18:10",
"reflection":"God is a place of safety and protection."
},

{
"text":"The Lord is faithful, and He will strengthen you and protect you.",
"ref":"2 Thessalonians 3:3",
"reflection":"God's faithfulness gives us security."
},

{
"text":"I have hidden Your word in my heart that I might not sin against You.",
"ref":"Psalm 119:11",
"reflection":"God's Word strengthens our decisions and character."
},

{
"text":"The battle is not yours, but God's.",
"ref":"2 Chronicles 20:15",
"reflection":"Some struggles require surrender rather than striving."
}

],

"hope": [

{
"text":"For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future.",
"ref":"Jeremiah 29:11",
"reflection":"Even when the future feels uncertain, God is still working with purpose."
},

{
"text":"Weeping may endure for a night, but joy comes in the morning.",
"ref":"Psalm 30:5",
"reflection":"Difficult seasons do not last forever. God brings renewal."
},

{
"text":"The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
"ref":"Psalm 34:18",
"reflection":"God is near when your heart feels heavy."
},

{
"text":"Cast all your anxiety on Him because He cares for you.",
"ref":"1 Peter 5:7",
"reflection":"You do not have to carry every burden alone."
},

{
"text":"Come to me, all you who are weary and burdened, and I will give you rest.",
"ref":"Matthew 11:28",
"reflection":"Jesus invites us to find rest instead of carrying everything ourselves."
},

{
"text":"The Lord is good, a refuge in times of trouble. He cares for those who trust in Him.",
"ref":"Nahum 1:7",
"reflection":"God remains a safe place during difficult moments."
},

{
"text":"Those who sow with tears will reap with songs of joy.",
"ref":"Psalm 126:5",
"reflection":"Pain can become part of a story of growth and restoration."
},

{
"text":"I will restore to you the years that the locust has eaten.",
"ref":"Joel 2:25",
"reflection":"God is able to restore what has been lost."
},

{
"text":"Because of the Lord's great love we are not consumed, for His compassions never fail. They are new every morning.",
"ref":"Lamentations 3:22-23",
"reflection":"Every day is a new opportunity because God's mercy is renewed."
},

{
"text":"The Lord upholds all who fall and lifts up all who are bowed down.",
"ref":"Psalm 145:14",
"reflection":"God helps us rise after moments of failure."
},

{
"text":"The righteous fall seven times, and rise again.",
"ref":"Proverbs 24:16",
"reflection":"Failure is not the end. Growth comes from getting back up."
},

{
"text":"May the God of hope fill you with all joy and peace as you trust in Him.",
"ref":"Romans 15:13",
"reflection":"Hope grows when we place our trust in God."
},

{
"text":"Do not let your hearts be troubled. You believe in God; believe also in me.",
"ref":"John 14:1",
"reflection":"Jesus offers peace when life feels overwhelming."
},

{
"text":"I lift up my eyes to the mountains. Where does my help come from? My help comes from the Lord.",
"ref":"Psalm 121:1-2",
"reflection":"God is the source of true help and direction."
},

{
"text":"The Lord your God is with you, the Mighty Warrior who saves. He will take great delight in you.",
"ref":"Zephaniah 3:17",
"reflection":"God's love reminds us that we are not forgotten."
},

{
"text":"Let us not become weary in doing good, for at the proper time we will reap a harvest if we do not give up.",
"ref":"Galatians 6:9",
"reflection":"Consistency matters. Keep going even when results are slow."
},

{
"text":"My soul finds rest in God alone; my salvation comes from Him.",
"ref":"Psalm 62:1",
"reflection":"Peace comes from trusting God rather than circumstances."
},

{
"text":"The Lord is my shepherd, I lack nothing.",
"ref":"Psalm 23:1",
"reflection":"God provides guidance, care and direction."
},

{
"text":"You will keep in perfect peace those whose minds are steadfast, because they trust in You.",
"ref":"Isaiah 26:3",
"reflection":"A focused mind on God brings stability."
},

{
"text":"After you have suffered for a little while, the God of all grace will restore you and make you strong, firm and steadfast.",
"ref":"1 Peter 5:10",
"reflection":"God uses difficult seasons to build endurance."
}

],

"anxiety": [

{
"text":"Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God.",
"ref":"Philippians 4:6",
"reflection":"Instead of carrying anxiety alone, bring your worries to God through prayer."
},

{
"text":"And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
"ref":"Philippians 4:7",
"reflection":"God's peace can remain even when circumstances are difficult."
},

{
"text":"When anxiety was great within me, Your consolation brought me joy.",
"ref":"Psalm 94:19",
"reflection":"God brings comfort when your thoughts feel overwhelming."
},

{
"text":"Be still, and know that I am God.",
"ref":"Psalm 46:10",
"reflection":"Sometimes the answer is not doing more, but trusting more."
},

{
"text":"You will keep in perfect peace those whose minds are steadfast, because they trust in You.",
"ref":"Isaiah 26:3",
"reflection":"A mind focused on God finds stability in stressful seasons."
},

{
"text":"Trust in the Lord with all your heart and lean not on your own understanding.",
"ref":"Proverbs 3:5",
"reflection":"You do not need to understand everything before trusting God."
},

{
"text":"Commit to the Lord whatever you do, and He will establish your plans.",
"ref":"Proverbs 16:3",
"reflection":"Give your goals and studies to God and allow Him to guide your path."
},

{
"text":"Cast your cares on the Lord and He will sustain you; He will never let the righteous be shaken.",
"ref":"Psalm 55:22",
"reflection":"God is strong enough to carry the burdens you cannot."
},

{
"text":"The Lord gives strength to His people; the Lord blesses His people with peace.",
"ref":"Psalm 29:11",
"reflection":"God provides both strength for challenges and peace for the journey."
},

{
"text":"Peace I leave with you; My peace I give you. I do not give to you as the world gives.",
"ref":"John 14:27",
"reflection":"Jesus offers a peace that is deeper than temporary solutions."
},

{
"text":"Do not worry about tomorrow, for tomorrow will worry about itself. Each day has enough trouble of its own.",
"ref":"Matthew 6:34",
"reflection":"Focus on today's responsibilities instead of being consumed by tomorrow."
},

{
"text":"Your faithfulness continues through all generations; You established the earth, and it endures.",
"ref":"Psalm 119:90",
"reflection":"God's consistency gives us confidence when life feels unstable."
},

{
"text":"The Lord is good to those whose hope is in Him, to the one who seeks Him.",
"ref":"Lamentations 3:25",
"reflection":"Seeking God brings hope even while waiting."
},

{
"text":"The Lord will fight for you; you need only to be still.",
"ref":"Exodus 14:14",
"reflection":"Not every battle is won through effort. Some are won through surrender."
},

{
"text":"My grace is sufficient for you, for My power is made perfect in weakness.",
"ref":"2 Corinthians 12:9",
"reflection":"God's strength appears most clearly when we feel weak."
},

{
"text":"In peace I will lie down and sleep, for You alone, Lord, make me dwell in safety.",
"ref":"Psalm 4:8",
"reflection":"God gives rest to a heart that trusts Him."
},

{
"text":"The Lord is my helper; I will not be afraid.",
"ref":"Hebrews 13:6",
"reflection":"Fear loses its power when we remember God is present."
},

{
"text":"Let the peace of Christ rule in your hearts.",
"ref":"Colossians 3:15",
"reflection":"Allow God's peace to guide your thoughts and decisions."
},

{
"text":"Humble yourselves, therefore, under God's mighty hand, that He may lift you up in due time.",
"ref":"1 Peter 5:6",
"reflection":"Trust God's timing instead of being controlled by pressure."
},

{
"text":"The name of the Lord is a strong tower; the righteous run to it and are safe.",
"ref":"Proverbs 18:10",
"reflection":"God is a place of safety when life feels uncertain."
}

],

"exams": [

{
"text":"If any of you lacks wisdom, you should ask God, who gives generously to all without finding fault, and it will be given to you.",
"ref":"James 1:5",
"reflection":"Ask God for understanding and wisdom as you learn."
},

{
"text":"The beginning of wisdom is this: Get wisdom. Though it cost all you have, get understanding.",
"ref":"Proverbs 4:7",
"reflection":"Learning and understanding are valuable treasures worth pursuing."
},

{
"text":"The plans of the diligent lead surely to abundance, but everyone who is hasty comes only to poverty.",
"ref":"Proverbs 21:5",
"reflection":"Consistent preparation produces better results than last-minute pressure."
},

{
"text":"Whatever you do, work at it with all your heart, as working for the Lord, not for human masters.",
"ref":"Colossians 3:23",
"reflection":"Your studies can be an act of dedication and worship."
},

{
"text":"Commit your work to the Lord, and your plans will be established.",
"ref":"Proverbs 16:3",
"reflection":"Invite God into your academic goals and decisions."
},

{
"text":"A wise person is hungry for knowledge, while the fool feeds on trash.",
"ref":"Proverbs 15:14",
"reflection":"Develop a desire to keep learning and growing."
},

{
"text":"The wise store up knowledge, but the mouth of a fool invites ruin.",
"ref":"Proverbs 10:14",
"reflection":"Knowledge grows when you intentionally seek and preserve it."
},

{
"text":"Do your best to present yourself to God as one approved, a worker who does not need to be ashamed and who correctly handles the word of truth.",
"ref":"2 Timothy 2:15",
"reflection":"Excellence comes from dedication, preparation and discipline."
},

{
"text":"She sets about her work vigorously; her arms are strong for her tasks.",
"ref":"Proverbs 31:17",
"reflection":"Approach your responsibilities with strength and commitment."
},

{
"text":"The hardworking farmer should be the first to receive a share of the crops.",
"ref":"2 Timothy 2:6",
"reflection":"Effort and patience eventually produce results."
},

{
"text":"Those who sow with tears will reap with songs of joy.",
"ref":"Psalm 126:5",
"reflection":"Difficult seasons of studying can lead to joyful outcomes."
},

{
"text":"Do not despise these small beginnings, for the Lord rejoices to see the work begin.",
"ref":"Zechariah 4:10",
"reflection":"Small study sessions still matter. Progress is built one step at a time."
},

{
"text":"Let the wise listen and add to their learning, and let the discerning get guidance.",
"ref":"Proverbs 1:5",
"reflection":"Growth comes from remaining teachable."
},

{
"text":"Teach me knowledge and good judgment, for I trust your commands.",
"ref":"Psalm 119:66",
"reflection":"Ask God to guide your understanding and decisions."
},

{
"text":"I can do all things through Christ who strengthens me.",
"ref":"Philippians 4:13",
"reflection":"God gives strength when challenges feel bigger than you."
},

{
"text":"The Lord gives wisdom; from His mouth come knowledge and understanding.",
"ref":"Proverbs 2:6",
"reflection":"True wisdom begins with God."
},

{
"text":"Whatever you have learned or received or heard from me, or seen in me, put it into practice. And the God of peace will be with you.",
"ref":"Philippians 4:9",
"reflection":"Growth happens when knowledge becomes action."
},

{
"text":"A wise man will hear and increase in learning, and a man of understanding will acquire wise counsel.",
"ref":"Proverbs 1:5",
"reflection":"Never stop learning, even after success."
},

{
"text":"Work hard and become a leader; be lazy and become a slave.",
"ref":"Proverbs 12:24",
"reflection":"Discipline creates opportunities."
},

{
"text":"May the favor of the Lord our God rest on us; establish the work of our hands for us.",
"ref":"Psalm 90:17",
"reflection":"Ask God to bless the work and effort you put in."
},

{
"text":"The hand of the diligent will rule, while the lazy will be put to forced labor.",
"ref":"Proverbs 12:24",
"reflection":"Consistency and effort build excellence."
},

{
"text":"Whatever is true, whatever is noble, whatever is right, whatever is pure, whatever is lovely, whatever is admirable, think about such things.",
"ref":"Philippians 4:8",
"reflection":"Protect your thoughts during stressful academic seasons."
},

{
"text":"Run in such a way as to take the prize.",
"ref":"1 Corinthians 9:24",
"reflection":"Approach your goals with commitment and purpose."
},

{
"text":"I have hidden Your word in my heart that I might not sin against You.",
"ref":"Psalm 119:11",
"reflection":"Storing wisdom within you helps guide your choices."
},

{
"text":"The soul of the diligent is richly supplied.",
"ref":"Proverbs 13:4",
"reflection":"Persistent effort brings growth and reward."
}

],

"purpose": [

{
"text":"For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future.",
"ref":"Jeremiah 29:11",
"reflection":"God's plans for your life are filled with hope, even when the future feels uncertain."
},

{
"text":"Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to Him, and He will make your paths straight.",
"ref":"Proverbs 3:5-6",
"reflection":"God guides those who surrender their plans to Him."
},

{
"text":"We are God's handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do.",
"ref":"Ephesians 2:10",
"reflection":"Your life has purpose and your gifts have meaning."
},

{
"text":"Before I formed you in the womb I knew you, before you were born I set you apart.",
"ref":"Jeremiah 1:5",
"reflection":"Your existence is intentional. God knew you before anyone else did."
},

{
"text":"Delight yourself in the Lord, and He will give you the desires of your heart.",
"ref":"Psalm 37:4",
"reflection":"When your heart aligns with God, your desires become shaped by His purpose."
},

{
"text":"Many are the plans in a person's heart, but it is the Lord's purpose that prevails.",
"ref":"Proverbs 19:21",
"reflection":"Make plans, but remember God directs the ultimate outcome."
},

{
"text":"The steps of a good person are ordered by the Lord, and He delights in their way.",
"ref":"Psalm 37:23",
"reflection":"Even small steps are guided by God."
},

{
"text":"Commit to the Lord whatever you do, and He will establish your plans.",
"ref":"Proverbs 16:3",
"reflection":"Invite God into your goals, studies and future decisions."
},

{
"text":"You will seek Me and find Me when you seek Me with all your heart.",
"ref":"Jeremiah 29:13",
"reflection":"A closer relationship with God brings clarity and direction."
},

{
"text":"The Lord will fulfill His purpose for me; Your love, Lord, endures forever.",
"ref":"Psalm 138:8",
"reflection":"God is still working even when progress feels slow."
},

{
"text":"A person's heart plans his way, but the Lord determines his steps.",
"ref":"Proverbs 16:9",
"reflection":"Plans are important, but remain open to God's guidance."
},

{
"text":"Where there is no vision, the people perish.",
"ref":"Proverbs 29:18",
"reflection":"A clear vision helps you move forward with purpose."
},

{
"text":"Let us not become weary in doing good, for at the proper time we will reap a harvest if we do not give up.",
"ref":"Galatians 6:9",
"reflection":"Purpose requires patience and perseverance."
},

{
"text":"The purpose of a person's heart are deep waters, but one who has insight draws them out.",
"ref":"Proverbs 20:5",
"reflection":"Discovering your purpose takes reflection and wisdom."
},

{
"text":"Whatever you do, do it all for the glory of God.",
"ref":"1 Corinthians 10:31",
"reflection":"Your everyday actions can honour God."
},

{
"text":"I praise You because I am fearfully and wonderfully made; Your works are wonderful, I know that full well.",
"ref":"Psalm 139:14",
"reflection":"Your worth comes from God, not achievements or opinions."
},

{
"text":"The Lord is my shepherd, I lack nothing.",
"ref":"Psalm 23:1",
"reflection":"God provides what you need as you follow His direction."
},

{
"text":"Your word is a lamp for my feet, a light on my path.",
"ref":"Psalm 119:105",
"reflection":"God may not reveal the whole journey, but He provides enough light for the next step."
},

{
"text":"Acknowledge Him in all your ways, and He will make your paths straight.",
"ref":"Proverbs 3:6",
"reflection":"Include God in every decision, both big and small."
},

{
"text":"The plans of the Lord stand firm forever, the purposes of His heart through all generations.",
"ref":"Psalm 33:11",
"reflection":"God's purpose remains steady even when life changes."
},

{
"text":"You are the light of the world. A town built on a hill cannot be hidden.",
"ref":"Matthew 5:14",
"reflection":"You were created to make an impact around you."
},

{
"text":"Rise up; this matter is in your hands. We will support you, so take courage and do it.",
"ref":"Ezra 10:4",
"reflection":"God gives courage to take action when opportunities appear."
},

{
"text":"Be strong and courageous. Do not be afraid or terrified because of them, for the Lord your God goes with you.",
"ref":"Deuteronomy 31:6",
"reflection":"You do not walk into your future alone."
},

{
"text":"The Lord directs the steps of the godly. He delights in every detail of their lives.",
"ref":"Psalm 37:23",
"reflection":"God cares about the details of your journey."
}

],

"relationships": [

{
"text":"Walk with the wise and become wise, for a companion of fools suffers harm.",
"ref":"Proverbs 13:20",
"reflection":"The people around you influence your growth, choices and character."
},

{
"text":"A friend loves at all times, and a brother is born for a time of adversity.",
"ref":"Proverbs 17:17",
"reflection":"True friendship remains present during difficult seasons."
},

{
"text":"Greater love has no one than this: to lay down one's life for one's friends.",
"ref":"John 15:13",
"reflection":"Love is shown through sacrifice, care and commitment."
},

{
"text":"Two are better than one, because they have a good return for their labor.",
"ref":"Ecclesiastes 4:9",
"reflection":"God created us to grow through meaningful relationships."
},

{
"text":"As iron sharpens iron, so one person sharpens another.",
"ref":"Proverbs 27:17",
"reflection":"The right people help you become better."
},

{
"text":"Do to others as you would have them do to you.",
"ref":"Luke 6:31",
"reflection":"Treat others with the kindness and respect you desire."
},

{
"text":"Be kind and compassionate to one another, forgiving each other, just as in Christ God forgave you.",
"ref":"Ephesians 4:32",
"reflection":"Forgiveness creates freedom and restores relationships."
},

{
"text":"Above all, love each other deeply, because love covers over a multitude of sins.",
"ref":"1 Peter 4:8",
"reflection":"Love chooses grace even when people make mistakes."
},

{
"text":"A gentle answer turns away wrath, but a harsh word stirs up anger.",
"ref":"Proverbs 15:1",
"reflection":"Wisdom is shown through how we communicate."
},

{
"text":"Let everything you do be done in love.",
"ref":"1 Corinthians 16:14",
"reflection":"Love should guide our actions and words."
},

{
"text":"Make every effort to keep the unity of the Spirit through the bond of peace.",
"ref":"Ephesians 4:3",
"reflection":"Healthy relationships require humility and effort."
},

{
"text":"Do not be misled: Bad company corrupts good character.",
"ref":"1 Corinthians 15:33",
"reflection":"Choose friendships that encourage growth and godly character."
},

{
"text":"The righteous choose their friends carefully, but the way of the wicked leads them astray.",
"ref":"Proverbs 12:26",
"reflection":"Not every connection is beneficial for your journey."
},

{
"text":"Encourage one another and build each other up, just as in fact you are doing.",
"ref":"1 Thessalonians 5:11",
"reflection":"Your words can strengthen someone who is struggling."
},

{
"text":"Carry each other's burdens, and in this way you will fulfill the law of Christ.",
"ref":"Galatians 6:2",
"reflection":"Support and compassion are powerful expressions of love."
},

{
"text":"A gossip betrays a confidence, but a trustworthy person keeps a secret.",
"ref":"Proverbs 11:13",
"reflection":"Trust grows when we respect the vulnerability of others."
},

{
"text":"Love is patient, love is kind. It does not envy, it does not boast, it is not proud.",
"ref":"1 Corinthians 13:4",
"reflection":"Godly love is shown through patience and humility."
},

{
"text":"Love does not delight in evil but rejoices with the truth.",
"ref":"1 Corinthians 13:6",
"reflection":"Real love celebrates honesty and goodness."
},

{
"text":"My command is this: Love each other as I have loved you.",
"ref":"John 15:12",
"reflection":"Jesus teaches us a love that is selfless and intentional."
},

{
"text":"A perverse person stirs up conflict, but a trustworthy person keeps a secret.",
"ref":"Proverbs 11:13",
"reflection":"Being trustworthy protects relationships."
},

{
"text":"Blessed are the peacemakers, for they will be called children of God.",
"ref":"Matthew 5:9",
"reflection":"Creating peace reflects God's character."
},

{
"text":"If it is possible, as far as it depends on you, live at peace with everyone.",
"ref":"Romans 12:18",
"reflection":"Do your part to create healthy relationships."
},

{
"text":"Be completely humble and gentle; be patient, bearing with one another in love.",
"ref":"Ephesians 4:2",
"reflection":"Strong relationships require patience and understanding."
},

{
"text":"Two people are better off than one, for they can help each other succeed.",
"ref":"Ecclesiastes 4:9",
"reflection":"The right community helps you reach your goals."
},

{
"text":"A true friend sticks by you in times of trouble.",
"ref":"Proverbs 18:24",
"reflection":"Real friendships are revealed through loyalty and support."
}

],

"healing": [

{
"text":"He heals the brokenhearted and binds up their wounds.",
"ref":"Psalm 147:3",
"reflection":"God sees your pain and brings healing to wounded hearts."
},

{
"text":"He gives strength to the weary and increases the power of the weak.",
"ref":"Isaiah 40:29",
"reflection":"God provides strength when you feel exhausted."
},

{
"text":"Forget the former things; do not dwell on the past. See, I am doing a new thing!",
"ref":"Isaiah 43:18-19",
"reflection":"Your past does not have the final word. God can create something new."
},

{
"text":"Therefore, if anyone is in Christ, the new creation has come: The old has gone, the new is here!",
"ref":"2 Corinthians 5:17",
"reflection":"God offers a fresh start and a renewed identity."
},

{
"text":"As far as the east is from the west, so far has He removed our transgressions from us.",
"ref":"Psalm 103:12",
"reflection":"God's forgiveness removes the weight of guilt."
},

{
"text":"Come to Me, all you who are weary and burdened, and I will give you rest.",
"ref":"Matthew 11:28",
"reflection":"Jesus invites you to bring your burdens to Him."
},

{
"text":"The Lord is close to the brokenhearted and saves those who are crushed in spirit.",
"ref":"Psalm 34:18",
"reflection":"God is near during seasons of heartbreak and difficulty."
},

{
"text":"A time to weep and a time to laugh, a time to mourn and a time to dance.",
"ref":"Ecclesiastes 3:4",
"reflection":"Every season has a purpose. Healing takes time."
},

{
"text":"Create in me a pure heart, O God, and renew a steadfast spirit within me.",
"ref":"Psalm 51:10",
"reflection":"God can transform your heart and renew your desires."
},

{
"text":"The Lord sustains them on their sickbed and restores them from their bed of illness.",
"ref":"Psalm 41:3",
"reflection":"God cares about your restoration and wellbeing."
},

{
"text":"My flesh and my heart may fail, but God is the strength of my heart and my portion forever.",
"ref":"Psalm 73:26",
"reflection":"Even when you feel weak, God remains your source of strength."
},

{
"text":"He has made everything beautiful in its time.",
"ref":"Ecclesiastes 3:11",
"reflection":"God can bring beauty from seasons that feel broken."
},

{
"text":"The Lord is compassionate and gracious, slow to anger, abounding in love.",
"ref":"Psalm 103:8",
"reflection":"God's character is full of mercy and patience."
},

{
"text":"Repent, then, and turn to God, so that your sins may be wiped out.",
"ref":"Acts 3:19",
"reflection":"Turning back to God opens the door to renewal."
},

{
"text":"If we confess our sins, He is faithful and just and will forgive us our sins and purify us from all unrighteousness.",
"ref":"1 John 1:9",
"reflection":"God offers forgiveness when we come to Him honestly."
},

{
"text":"The Lord will fight for you; you need only to be still.",
"ref":"Exodus 14:14",
"reflection":"You do not have to fight every battle alone."
},

{
"text":"Those who sow with tears will reap with songs of joy.",
"ref":"Psalm 126:5",
"reflection":"Painful seasons can produce beautiful growth."
},

{
"text":"I will restore to you the years that the locust has eaten.",
"ref":"Joel 2:25",
"reflection":"God is able to restore what feels lost."
},

{
"text":"Weeping may endure for a night, but joy comes in the morning.",
"ref":"Psalm 30:5",
"reflection":"Hard seasons do not last forever."
},

{
"text":"Do not be overcome by evil, but overcome evil with good.",
"ref":"Romans 12:21",
"reflection":"Choose healing instead of allowing hurt to control you."
},

{
"text":"Be strong and take heart, all you who hope in the Lord.",
"ref":"Psalm 31:24",
"reflection":"Hope gives courage to keep moving forward."
},

{
"text":"The Lord makes firm the steps of the one who delights in Him.",
"ref":"Psalm 37:23",
"reflection":"God guides you even while rebuilding your life."
},

{
"text":"I have loved you with an everlasting love; I have drawn you with unfailing kindness.",
"ref":"Jeremiah 31:3",
"reflection":"God's love remains constant through every season."
},

{
"text":"A broken and contrite heart God will not despise.",
"ref":"Psalm 51:17",
"reflection":"God welcomes honesty and humility."
},

{
"text":"The God of all grace, who called you to His eternal glory in Christ, will Himself restore you and make you strong.",
"ref":"1 Peter 5:10",
"reflection":"God restores, strengthens and rebuilds."
}

],

"faith": [

{
"text":"Trust in Him at all times, you people; pour out your hearts to Him, for God is our refuge.",
"ref":"Psalm 62:8",
"reflection":"God invites you to bring every fear, dream and struggle to Him."
},

{
"text":"The Lord is my rock, my fortress and my deliverer; my God is my rock, in whom I take refuge.",
"ref":"Psalm 18:2",
"reflection":"God is a secure foundation when life feels uncertain."
},

{
"text":"Those who know Your name trust in You, for You, Lord, have never forsaken those who seek You.",
"ref":"Psalm 9:10",
"reflection":"God remains faithful to those who seek Him."
},

{
"text":"Now faith is confidence in what we hope for and assurance about what we do not see.",
"ref":"Hebrews 11:1",
"reflection":"Faith means trusting God even when the outcome is unclear."
},

{
"text":"Without faith it is impossible to please God, because anyone who comes to Him must believe that He exists and that He rewards those who earnestly seek Him.",
"ref":"Hebrews 11:6",
"reflection":"Faith grows when we intentionally seek God."
},

{
"text":"The Lord is good, a refuge in times of trouble. He cares for those who trust in Him.",
"ref":"Nahum 1:7",
"reflection":"God is a safe place during difficult moments."
},

{
"text":"Be still before the Lord and wait patiently for Him.",
"ref":"Psalm 37:7",
"reflection":"Waiting on God requires patience and trust."
},

{
"text":"The Lord is faithful to all His promises and loving toward all He has made.",
"ref":"Psalm 145:13",
"reflection":"God's promises can be trusted because His character is faithful."
},

{
"text":"Jesus Christ is the same yesterday and today and forever.",
"ref":"Hebrews 13:8",
"reflection":"God's nature does not change even when circumstances do."
},

{
"text":"Every good and perfect gift is from above, coming down from the Father of the heavenly lights.",
"ref":"James 1:17",
"reflection":"Recognize God's goodness in the blessings around you."
},

{
"text":"Give thanks to the Lord, for He is good; His love endures forever.",
"ref":"Psalm 107:1",
"reflection":"Gratitude strengthens your awareness of God's presence."
},

{
"text":"Pray continually.",
"ref":"1 Thessalonians 5:17",
"reflection":"Prayer is an ongoing relationship with God, not just a last resort."
},

{
"text":"Call to Me and I will answer you and tell you great and unsearchable things you do not know.",
"ref":"Jeremiah 33:3",
"reflection":"God invites you to seek Him for wisdom and direction."
},

{
"text":"Draw near to God and He will draw near to you.",
"ref":"James 4:8",
"reflection":"A closer relationship with God begins with intentionally seeking Him."
},

{
"text":"The Lord is near to all who call on Him, to all who call on Him in truth.",
"ref":"Psalm 145:18",
"reflection":"God hears sincere prayers."
},

{
"text":"I sought the Lord, and He answered me; He delivered me from all my fears.",
"ref":"Psalm 34:4",
"reflection":"God responds when we turn to Him."
},

{
"text":"Commit your way to the Lord; trust in Him and He will do this.",
"ref":"Psalm 37:5",
"reflection":"Surrendering your plans allows God to guide your path."
},

{
"text":"Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.",
"ref":"Joshua 1:9",
"reflection":"God's presence gives courage for every challenge."
},

{
"text":"The Lord is my light and my salvation; whom shall I fear?",
"ref":"Psalm 27:1",
"reflection":"God's presence replaces fear with confidence."
},

{
"text":"I will instruct you and teach you in the way you should go; I will counsel you with My loving eye on you.",
"ref":"Psalm 32:8",
"reflection":"God provides guidance when you seek Him."
},

{
"text":"The name of the Lord is a fortified tower; the righteous run to it and are safe.",
"ref":"Proverbs 18:10",
"reflection":"God is a place of safety and protection."
},

{
"text":"My grace is sufficient for you, for My power is made perfect in weakness.",
"ref":"2 Corinthians 12:9",
"reflection":"God's strength works through our limitations."
},

{
"text":"Let us hold unswervingly to the hope we profess, for He who promised is faithful.",
"ref":"Hebrews 10:23",
"reflection":"Keep trusting because God's promises remain dependable."
},

{
"text":"The Lord bless you and keep you; the Lord make His face shine on you and be gracious to you.",
"ref":"Numbers 6:24-25",
"reflection":"God's blessing and presence surround His people."
},

{
"text":"May the God of hope fill you with all joy and peace as you trust in Him.",
"ref":"Romans 15:13",
"reflection":"Trusting God produces hope, joy and peace."
}

],

"courage": [

{
"text":"Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go.",
"ref":"Joshua 1:9",
"reflection":"Courage comes from knowing God is present wherever you go."
},

{
"text":"When I am afraid, I put my trust in You.",
"ref":"Psalm 56:3",
"reflection":"Fear does not have to control you when you place your trust in God."
},

{
"text":"The Lord is my helper; I will not be afraid. What can mere mortals do to me?",
"ref":"Hebrews 13:6",
"reflection":"God's presence gives confidence beyond human circumstances."
},

{
"text":"For God has not given us a spirit of fear, but of power and of love and of a sound mind.",
"ref":"2 Timothy 1:7",
"reflection":"Fear does not define you. God gives strength, love and wisdom."
},

{
"text":"The righteous are as bold as a lion.",
"ref":"Proverbs 28:1",
"reflection":"A life built on God creates confidence and courage."
},

{
"text":"The Lord will go before you. He will be with you; He will never leave you nor forsake you.",
"ref":"Deuteronomy 31:8",
"reflection":"You never step into the unknown alone."
},

{
"text":"Do not fear, for I am with you; do not be dismayed, for I am your God.",
"ref":"Isaiah 41:10",
"reflection":"God's presence is greater than your fears."
},

{
"text":"I can do all things through Christ who strengthens me.",
"ref":"Philippians 4:13",
"reflection":"God provides strength for challenges that seem impossible."
},

{
"text":"The Lord is my strength and my shield; my heart trusts in Him, and He helps me.",
"ref":"Psalm 28:7",
"reflection":"Trusting God brings strength when you feel weak."
},

{
"text":"Be strong and take heart, all you who hope in the Lord.",
"ref":"Psalm 31:24",
"reflection":"Hope gives you courage to keep moving forward."
},

{
"text":"The angel of the Lord encamps around those who fear Him, and He delivers them.",
"ref":"Psalm 34:7",
"reflection":"God watches over those who seek Him."
},

{
"text":"The Lord gives strength to His people; the Lord blesses His people with peace.",
"ref":"Psalm 29:11",
"reflection":"God gives both courage and calm in difficult situations."
},

{
"text":"The Lord is with me; I will not be afraid. What can anyone do to me?",
"ref":"Psalm 118:6",
"reflection":"God's presence removes the power of fear."
},

{
"text":"Even though I walk through the darkest valley, I will fear no evil, for You are with me.",
"ref":"Psalm 23:4",
"reflection":"God walks with you through every difficult season."
},

{
"text":"The name of the Lord is a strong tower; the righteous run to it and are safe.",
"ref":"Proverbs 18:10",
"reflection":"God is a place of security when life feels overwhelming."
},

{
"text":"Wait for the Lord; be strong and take heart and wait for the Lord.",
"ref":"Psalm 27:14",
"reflection":"Courage also means patiently trusting God's timing."
},

{
"text":"The Lord fights for you; you need only to be still.",
"ref":"Exodus 14:14",
"reflection":"Some battles are won by trusting God rather than relying only on yourself."
},

{
"text":"Do not be afraid of them; the Lord your God Himself will fight for you.",
"ref":"Deuteronomy 3:22",
"reflection":"God supports you when you face opposition."
},

{
"text":"The Lord is faithful, and He will strengthen you and protect you from the evil one.",
"ref":"2 Thessalonians 3:3",
"reflection":"God provides protection and strength."
},

{
"text":"The righteous cry out, and the Lord hears them; He delivers them from all their troubles.",
"ref":"Psalm 34:17",
"reflection":"God listens when you call on Him."
},

{
"text":"You will not fear the terror of night, nor the arrow that flies by day.",
"ref":"Psalm 91:5",
"reflection":"God provides security even in uncertain moments."
},

{
"text":"I have set the Lord always before me; because He is at my right hand, I will not be shaken.",
"ref":"Psalm 16:8",
"reflection":"Keeping God at the center creates stability."
},

{
"text":"The Lord is good, a refuge in times of trouble.",
"ref":"Nahum 1:7",
"reflection":"God remains a safe place during difficult circumstances."
},

{
"text":"Do not be overcome by evil, but overcome evil with good.",
"ref":"Romans 12:21",
"reflection":"Courage chooses what is right even when it is difficult."
},

{
"text":"Those who hope in the Lord will renew their strength. They will soar on wings like eagles.",
"ref":"Isaiah 40:31",
"reflection":"God renews those who place their hope in Him."
}

],

"gratitude": [

{
"text":"Give thanks to the Lord, for He is good; His love endures forever.",
"ref":"Psalm 136:1",
"reflection":"Gratitude reminds us of God's constant goodness."
},

{
"text":"Rejoice always, pray continually, give thanks in all circumstances; for this is God's will for you in Christ Jesus.",
"ref":"1 Thessalonians 5:16-18",
"reflection":"Joy and gratitude can exist even during difficult seasons."
},

{
"text":"This is the day the Lord has made; let us rejoice and be glad in it.",
"ref":"Psalm 118:24",
"reflection":"Each day is a gift worth appreciating."
},

{
"text":"A cheerful heart is good medicine, but a crushed spirit dries up the bones.",
"ref":"Proverbs 17:22",
"reflection":"Joy and positivity can strengthen your spirit."
},

{
"text":"The joy of the Lord is your strength.",
"ref":"Nehemiah 8:10",
"reflection":"True strength comes from the joy found in God."
},

{
"text":"Delight yourself in the Lord, and He will give you the desires of your heart.",
"ref":"Psalm 37:4",
"reflection":"When your heart aligns with God, your desires become transformed."
},

{
"text":"I have learned to be content whatever the circumstances.",
"ref":"Philippians 4:11",
"reflection":"Contentment is a skill we develop through trusting God."
},

{
"text":"Godliness with contentment is great gain.",
"ref":"1 Timothy 6:6",
"reflection":"A grateful heart values what truly matters."
},

{
"text":"Every good and perfect gift is from above.",
"ref":"James 1:17",
"reflection":"Recognize the blessings God places in your life."
},

{
"text":"Praise the Lord, my soul, and forget not all His benefits.",
"ref":"Psalm 103:2",
"reflection":"Remembering God's blessings changes your perspective."
},

{
"text":"Serve the Lord with gladness; come before Him with joyful songs.",
"ref":"Psalm 100:2",
"reflection":"Joy grows when we worship God."
},

{
"text":"The Lord has done great things for us, and we are filled with joy.",
"ref":"Psalm 126:3",
"reflection":"Look back and celebrate how far God has brought you."
},

{
"text":"May the God of hope fill you with all joy and peace as you trust in Him.",
"ref":"Romans 15:13",
"reflection":"Trust in God produces lasting joy and peace."
},

{
"text":"You make known to me the path of life; You will fill me with joy in Your presence.",
"ref":"Psalm 16:11",
"reflection":"God's presence is the greatest source of joy."
},

{
"text":"Let us come before Him with thanksgiving and extol Him with music and song.",
"ref":"Psalm 95:2",
"reflection":"Thankfulness draws our hearts closer to God."
}

],

"wisdom": [

{
"text":"If any of you lacks wisdom, you should ask God, who gives generously to all without finding fault.",
"ref":"James 1:5",
"reflection":"God welcomes your questions and gives wisdom freely."
},

{
"text":"Trust in the Lord with all your heart and lean not on your own understanding.",
"ref":"Proverbs 3:5",
"reflection":"God's wisdom is greater than our limited perspective."
},

{
"text":"In all your ways submit to Him, and He will make your paths straight.",
"ref":"Proverbs 3:6",
"reflection":"God guides those who surrender their plans to Him."
},

{
"text":"The beginning of wisdom is this: Get wisdom. Though it cost all you have, get understanding.",
"ref":"Proverbs 4:7",
"reflection":"Wisdom is one of life's greatest investments."
},

{
"text":"Teach us to number our days, that we may gain a heart of wisdom.",
"ref":"Psalm 90:12",
"reflection":"Wise people use their time intentionally."
},

{
"text":"Plans fail for lack of counsel, but with many advisers they succeed.",
"ref":"Proverbs 15:22",
"reflection":"Seeking guidance can lead to better decisions."
},

{
"text":"Commit to the Lord whatever you do, and He will establish your plans.",
"ref":"Proverbs 16:3",
"reflection":"Invite God into your goals and ambitions."
},

{
"text":"The heart of man plans his way, but the Lord establishes his steps.",
"ref":"Proverbs 16:9",
"reflection":"God can redirect your path according to His purpose."
},

{
"text":"A wise person is hungry for knowledge, while the fool feeds on trash.",
"ref":"Proverbs 15:14",
"reflection":"Keep growing by seeking truth and understanding."
},

{
"text":"Walk with the wise and become wise.",
"ref":"Proverbs 13:20",
"reflection":"Your environment shapes your growth."
},

{
"text":"The wise store up knowledge, but the mouth of a fool invites ruin.",
"ref":"Proverbs 10:14",
"reflection":"Learning and reflection build wisdom."
},

{
"text":"Listen to advice and accept discipline, and at the end you will be counted among the wise.",
"ref":"Proverbs 19:20",
"reflection":"Growth requires humility and willingness to learn."
},

{
"text":"Your word is a lamp for my feet, a light on my path.",
"ref":"Psalm 119:105",
"reflection":"God's truth provides direction when you are uncertain."
},

{
"text":"The plans of the diligent lead surely to abundance.",
"ref":"Proverbs 21:5",
"reflection":"Consistent effort creates opportunities."
},

{
"text":"May He give you the desire of your heart and make all your plans succeed.",
"ref":"Psalm 20:4",
"reflection":"God cares about the dreams and plans you carry."
}

]

}

ANCHIE_GUIDANCE = {

    "wisdom": {
        "thought": "Life brings many decisions, but you do not have to figure everything out alone. Ask God for wisdom and take each step with faith.",
        "step": "Take a few minutes today to think about one decision you need guidance on and pray about it."
    },


    "study": {
        "thought": "Learning takes patience. Every page you read and every concept you understand is progress.",
        "step": "Choose one topic today and spend focused time understanding it."
    },


    "peace": {
        "thought": "Stress can make challenges feel bigger than they are. Give your worries to God and focus on the next small step.",
        "step": "Take a short pause, breathe, pray and return to your work with a clearer mind."
    },


    "discipline": {
        "thought": "Growth is built through small choices repeated every day. Your habits shape your future.",
        "step": "Create a simple plan for your next study session and follow through."
    },


    "purpose": {
        "thought": "Your journey has meaning. Your studies are part of the gifts and purpose God is developing in you.",
        "step": "Write down one goal you want to work towards this season."
    },


    "hope": {
        "thought": "Difficult seasons do not define your whole story. Keep moving forward with faith and patience.",
        "step": "Write down one thing you are hopeful for today."
    },


    "prayer": {
        "thought": "Prayer is a place where you can bring your worries, dreams and questions to God.",
        "step": "Spend a few quiet minutes talking to God about your day."
    },


    "relationships": {
        "thought": "The people around you shape your journey. Choose kindness, forgiveness and wisdom in your relationships.",
        "step": "Think of one person you can encourage or appreciate today."
    }

}

def get_random_scripture(category=None):

    if category and category in scriptures:

        verses = scriptures[category]

    else:

        verses = []

        for group in scriptures.values():

            verses.extend(group)


    return random.choice(verses)
@scriptures.route("/scriptures")
def scriptures_page():

    category = request.args.get("category")

    if category and category in VERSE_LIBRARY:

        verse = random.choice(
            VERSE_LIBRARY[category]
        )

        scriptures_list = VERSE_LIBRARY[category]

    else:

        category = random.choice(
            list(VERSE_LIBRARY.keys())
        )

        verse = random.choice(
            VERSE_LIBRARY[category]
        )

        scriptures_list = VERSE_LIBRARY[category]


    reflection = verse["reflection"]


    guidance = ANCHIE_GUIDANCE.get(
        category,
        ANCHIE_GUIDANCE["wisdom"]
    )


    return render_template(
        "scriptures.html",
        verse=verse,
        reflection=reflection,
        scriptures=scriptures_list,
        anchie_thought=guidance["thought"],
        small_step=guidance["step"], 
        category=category
    )