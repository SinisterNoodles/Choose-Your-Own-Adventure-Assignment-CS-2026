story = {
    "startScene": {
        "art": "title",
        "text": (
            '''Once upon a time, there was a sweet little girl loved by everyone who met her—but most of all by her
grandmother. The old woman adored her so much that she made her a small red velvet hood. It suited her perfectly,
and from that day on, everyone called her Little Red Riding Hood.''',
            '''One morning, her mother said, “Come, Little Red Riding Hood, here’s a piece
of cake and a bottle of wine. Take them to your grandmother—she’s sick and weak, and this will do her good. Go before
it gets too hot, and remember to walk carefully. Don’t stray from the path, or you might fall and break the bottle. And
when you arrive, don’t forget to say good morning before you peek around her room.”''',
                 '''“I’ll be careful, Mother,” said Little Red Riding Hood, and she promised with a smile."''',
                 '''The grandmother lived deep in the forest, about half a league from the village.
Just as Little Red Riding Hood entered the woods, a wolf appeared on the path. She didn’t know what a wicked creature
he was and felt no fear at all.''',
                 '''“\033[1mGood morning, Little Red Riding Hood,”\033[0m said the wolf.'''
        ),
        "options": {
            "talk": "talkToWolf",
            "run": "runFromWolf",
        }
    },
    "talkToWolf": {
        "text": (
            '''\033[1m“Good morning, Mr. Wolf,”\033[0m she replied politely.''',
            '''\033[1m“Where are you going so early?”\033[0m he asked.''',
            '''\033[1m“To my grandmother’s house,”\033[0m said the girl.''',
            '''\033[1m“And what’s that in your basket?”\033[0m''',
            '''\033[1m“Cake and wine. Grandma’s been sick, so Mother sent me to cheer her up.”\033[0m''',
            '''\033[1m“And where does your grandmother live?”\033[0m asked the wolf.''',
            '''\033[1m“A little farther into the woods—under the three great oak trees, near the
hazel bushes. You must know it,”\033[0m she said.''',
                '''The wolf licked his lips and thought, What a tender young thing! She’ll taste even
better than the old woman. I’ll eat them both—but I’ll have to be clever about it.''',
                 '''He walked beside her for a bit, then said slyly, \033[1m“Look how pretty the flowers are here,
Little Red Riding Hood. Why not pick some for your grandmother? And listen—don’t you
hear how sweetly the birds are singing? You walk along so seriously, as if you were
going to school, when the forest is alive with joy!”\033[0m''',
                 '''Little Red Riding Hood looked up and saw sunlight dancing through the trees, making the
wildflowers sparkle. Grandma would love a bouquet, she thought. I still have plenty of time.
So she stepped off the path to gather flowers. Each time she picked one, she saw another even
prettier farther away, and she wandered deeper and deeper into the forest.''',
            '''Meanwhile, the wolf ran straight to the grandmother’s house and knocked at the door.''',
            '''\033[1m“Who’s there?”\033[0m called the grandmother.''',
            '''\033[1m“It’s me—Little Red Riding Hood,”\033[0m said the wolf sweetly. \033[1m“I’ve brought you cake and wine.”\033[0m'''
        ),
        "options": {
            "let her in": "letHerIn",
            "no wolf":"noWolf"
        }
    },
    "runFromWolf": {
        "text": (
            '''Little Red Riding Hood ran as fast as she could through the forest, her red cloak flapping behind her.''',
            '''The wolf, crouched low and eyes gleaming, sprinted after her, keeping just enough distance to stay unseen.''',
            '''\033[1m“Where are you going in such a hurry?”\033[0m he called after her slyly, but she ignored him and kept running.''',
            '''She dodged branches and leapt over roots, thinking only of her grandmother’s house.''',
            '''The wolf grinned, thinking, \033[1m“If I can reach her first, I’ll have a feast waiting.”\033[0m''',
            '''Panting, Little Red Riding Hood finally arrived at her grandmother’s cottage and dashed inside, slamming the door.''',
            '''The wolf skidded to the doorway moments later, his nose pressed against the wood, sniffing the air.''',
            '''\033[1m"Grandmother!"\033[0m Little Red Riding Hood called, catching her breath. "It’s me!"''',
            '''But before her grandmother could answer, the wolf tried the handle and found it locked. He circled the house, eyes fixed
on the windows, plotting how to get in.''',
            '''Little Red Riding Hood peeked through the curtains, heart pounding, and saw him lingering outside, waiting for a chance.''',
            '''She grabbed the basket of cake and wine, thinking quickly, and prepared to hide it where he could not find it.'''
        ),
        "options": {
            "find gun":"findGun",
            "find grandmother":"findGrandmother"
        }
    },
    "letHerIn": {
        "text": (
            '''\033[1m“Lift the latch,”\033[0m said the grandmother. \033[1m“I’m too weak to get up.”\033[0m''',
            '''The wolf lifted the latch, pushed open the door, and without a word, leapt upon the old woman and swallowed her whole.
Then he put on her nightgown and cap, pulled the curtains, and lay down in her bed.''',
            '''When Little Red Riding Hood finally reached the cottage, she was surprised to find the door standing open. The room felt
strange and quiet. \033[1m“Oh dear,”\033[0m she whispered, \033[1m“why do I feel so uneasy today?”\033[0m She called out, \033[1m“Good
morning, Grandma!”\033[0m but there was no answer.''',
            '''She went to the bed and drew back the curtains. There lay her grandmother, cap pulled low, face shadowed, looking quite odd.''',
            '''\033[1m“Oh, Grandma, what big ears you have!”\033[0m''',
            '''\033[1m“The better to hear you with, my child,”\033[0m came the growling reply.''',
            '''\033[1m“But, Grandma, what big eyes you have!”\033[0m''',
            '''\033[1m“The better to see you with, my dear.”\033[0m''',
            '''\033[1m“And what big hands you have!”\033[0m''',
            '''\033[1m“The better to hug you with.”\033[0m''',
            '''\033[1m“But, Grandma—what a terrible big mouth you have!”\033[0m'''
        ),
        "options": {
            "run from grandma":"runFromGrandma",
            "stay with grandma":"stayWithGrandma"
        }
    },
    "noWolf": {
        "text": (
'''\033[1m“No!”\033[0m she snapped. \033[1m“You will not come in, wolf!”\033[0m''',
'''The wolf snarled and slunk into a thick bush near the cottage, waiting and watching for Little Red Riding Hood.''',
'''When Little Red Riding Hood arrived, her grandmother called from the doorway, \033[1m“Come in, my dear!”\033[0m''',
'''As the door swung open, the wolf leapt from the bush, crashing toward the door with a terrifying growl. Grandma quickly
stepped aside, pulling Little Red Riding Hood in just in time.''',
'''The wolf, too fast to be stopped, smashed through a nearby window, shards of glass scattering across the floor, and
clambered into the room, eyes fixed on the girl.''',
'''Little Red Riding Hood froze, heart pounding, as the wolf prowled closer.'''
        ),
        "options": {
            "hug grandma":"hugGrandma",
            "run with grandma":"runWithGrandma"
        }
    },
    "findGun": {
        "text": (
            '''Little Red Riding Hood’s eyes fell on a hunting rifle propped in the corner, left by her grandfather.''',
            '''Her hands trembled as she lifted it, the weight both comforting and terrifying.''',
            '''\033[1m“I have to stop him… I have to save Grandma,”\033[0m she whispered to herself.''',
            '''Outside, the wolf circled the cottage, his ears twitching, unaware of her new weapon.''',
            '''She aimed through the window, trying to steady her breath, each heartbeat pounding in her ears.''',
            '''But as she fumbled with the gun, trying to load it, a cold realization struck—she had lost precious time.''',
            '''The wolf, seizing the moment, darted through the back door, which had been left slightly ajar.''',
            '''\033[1m"No!"\033[0m Little Red Riding Hood screamed as she spun around.''',
            '''The wolf lunged into the grandmother’s bedroom, and before Little Red Riding Hood could reach her, he struck.''',
            '''Her grandmother never had a chance; the wolf devoured her, leaving only silence and the scent of the forest.''',
            '''Little Red Riding Hood, frozen in horror, clutched the gun uselessly, the weight of it now a cruel reminder of her failure.''',
            '''Outside, the wolf emerged, licking his lips, eyes glinting with triumph as Little Red Riding Hood realized the danger was far from over.'''
        ),
        "options": {
            "run away":"runAwayFromWolfHouse",
            "shoot wolf":"shootWolf"
        }
    },
    "findGrandmother": {
        "text": (
            '''Her grandmother hurried from the back room, eyes wide with concern as she listened to the hurried warning.''',
            '''\033[1m“The wolf followed me here!”\033[0m Little Red Riding Hood whispered urgently. \033[1m“He’s outside, trying to get in!”\033[0m''',
            '''Grandmother nodded calmly, though her hands trembled, and pulled her granddaughter close.''',
            '''A sudden crash shook the cottage as the wolf hurled himself against the door, the wood splintering under the force.''',
            '''\033[1m“Stay behind me,”\033[0m Grandmother said firmly, placing herself between the door and Little Red Riding Hood.''',
            '''The hinges snapped, and the wolf burst into the cottage with a snarl, eyes locked onto the girl in the red cloak.''',
            '''Little Red Riding Hood stumbled backward, frozen with fear as the wolf lunged forward.''',
            '''In a swift motion, Grandmother stepped into his path, shouting, \033[1m“Run, child!”\033[0m''',
            '''The wolf collided with Grandmother instead, his jaws snapping as she pushed Little Red Riding Hood toward the back door.''',
            '''\033[1m“Don’t look back!”\033[0m she cried, holding the wolf’s attention as best she could.''',
            '''Tears streaming down her face, Little Red Riding Hood fled through the back door as the sounds of struggle filled the cottage.''',
            '''Outside, she ran into the forest once more, her grandmother’s brave sacrifice echoing in her mind.''',
            '''Behind her, the cottage fell silent, and the wolf’s low growl was the last sound she heard from within.'''
        ),
        "options": {
            "get revenge":"findGun",
            "go back home":"findGrandmother"
        }
    },
    "runFromGrandmother": {
        "text": (
            '''Little Red Riding Hood screamed and leapt away from the bed just as the wolf snapped his jaws where she had stood.
She darted across the room, her heart pounding, and ran toward the window as the wolf scrambled after her.''',
            '''In her panic, she fumbled with the latch and shoved the window open. Cold air rushed in. She began to climb out,
thinking only to escape into the forest below.''',
            '''But the wolf lunged forward with terrible speed. His claws caught her cloak and dragged her back inside before she
could slip through. With a single gulp, he swallowed her whole, just as he had her grandmother.''',
            '''The cottage fell silent. The wolf licked his lips, listened for a moment, and then bounded to the door. He fled into
the forest, vanishing between the trees before anyone could see him.''',
            '''A short while later, a lumberjack passing along the path noticed the cottage door ajar and the window hanging open.
He stepped inside and looked around at the disturbed room, the empty bed, and the broken latch.''',
            '''He called out, but there was no answer. The house stood still and hollow. And with the wolf long gone into the woods,
there was no one left who could save Little Red Riding Hood or her grandmother.'''
        ),
        "options": {}
    },
    "stayWithGrandma": {
        "text": (
            '''\033[1m“The better to eat you with!”\033[0m roared the wolf, and before she could scream, he sprang from the bed and swallowed Little Red Riding Hood whole.''',
            '''Full and satisfied, the wolf climbed back into bed and soon began to snore loudly. Just then, a passing huntsman heard the noise and muttered,
“That old woman snores like a beast! I should check on her.”''',
            '''He stepped inside and saw the wolf stretched out in the bed. \033[1m“So it’s you, you wicked creature!”\033[0m he said, raising his gun. But then he
thought, \033[1m*Maybe the old woman’s still inside.*\033[0m So instead of shooting, he took a pair of scissors and carefully cut open the wolf’s belly.''',
            '''After two careful snips, he saw a flash of red inside. A few more cuts—and out sprang Little Red Riding Hood, trembling but unharmed.
“Oh, how frightened I was! It was so dark inside!” she cried. Then the huntsman cut a little more, and out came the grandmother, pale but alive.''',
            '''To make sure the wolf could never harm anyone again, they filled his belly with heavy stones. When he awoke and tried to flee,
the weight pulled him down, and he fell dead on the spot.''',
            '''The huntsman skinned the wolf and went on his way. The grandmother ate her cake and drank her wine and soon felt much better.
As for Little Red Riding Hood, she thought to herself, \033[1m*From now on, I’ll never wander from the path again when Mother tells me not to.*\033[0m''',
            '''And from that day forward, Little Red Riding Hood never strayed from the path, and she lived happily ever after.'''
        ),
        "options": {}
    },
    "hugGrandma": {
        "text": (
            '''But instead of screaming, Little Red Riding Hood rushed past the wolf and threw her arms around her grandmother. \033[1m“Oh, Grandma, I was so frightened!”\033[0m she cried, hugging her tightly.''',
'''The wolf halted mid-step. The sight of the embrace stirred a memory long buried: a small wolf pup nuzzling against its own mother in a quiet den, safe and warm.''',
'''\033[1m“I… I remember,”\033[0m the wolf muttered, its growl fading into a whisper as the flashback passed through its mind.''',
'''Grandma peered over Little Red Riding Hood’s shoulder as the wolf lowered its head. \033[1m“I am sorry for the fright I caused you both,”\033[0m the wolf said softly.''',
'''Little Red Riding Hood turned, surprised by the change in the creature’s voice. \033[1m“Then you may stay, if you promise no more trouble,”\033[0m she replied cautiously.''',
'''The wolf nodded and, before anything else, carefully gathered wood and tools from outside. With patient effort, it repaired the broken window, fitting the frame back into place and sweeping away the glass.''',
'''As evening fell, Grandma set the table for three. The wolf sat politely by the hearth while a warm meal was prepared.''',
'''That night, the cottage was filled not with growls or fear, but with quiet conversation as they shared dinner together in unexpected peace.'''
        ),
        "options": {}
    }
}