# backend/app/fia_data.py

"""
Full FIA Data Structure: UNES Traits, Player Types, Relationships, and Scoring Logic
"""

# ========================== UNES TRAITS ==========================

UNES_TRAITS = {
    'Accountability': {
    'name': 'Accountability',
    'description': "Responsibility for one's actions, decisions, or mistakes",
    'scores': {
        0: "Blames others for everything – Always finds someone else to blame for their failures, mistakes, or shortcomings, no matter how minor the situation. Refuses to apologize – Never admits wrongdoing, even when it's clear they are at fault. Instead, they deflect or make excuses. Avoids responsibility at all costs – Always shifts responsibility to others, never stepping up to take charge or deal with the consequences of their actions.",
        2: "Shifts blame to others – Frequently blames others for their mistakes or failures, even when it is clear they are at least partially responsible. Denies responsibility for mistakes – Denies any involvement or accountability for things that go wrong, even if they were directly involved. Refuses to apologize – Avoids apologizing or acknowledging their role in a conflict or issue, often saying they did nothing wrong.",
        5: "Owns up to mistakes – Acknowledges when they've made a mistake or caused harm and takes responsibility without deflecting or blaming others. Apologizes sincerely – Offers a genuine apology when necessary, recognizing how their actions affected others and expressing remorse. Seeks solutions – When things go wrong, they actively work to fix the situation and make things right rather than avoiding or ignoring the issue.",
        8: "Frequent self-blame – Regularly blames themselves for minor issues or mistakes, even when others are equally responsible. Over-apologizing in small situations – Apologizes for things that are not their fault, like when a group project fails or someone else makes a mistake. Takes on too much responsibility – Voluntarily takes on tasks or problems that don't belong to them just to avoid conflict or to make others happy.",
        10: "Over-apologizes for minor issues – Apologizes excessively, even when the situation doesn't warrant it, and feels responsible for things beyond their control. Takes on blame that isn't theirs – Will accept fault for situations, even if it clearly isn't their responsibility or if others were at fault. Takes ownership of others' problems – Feels obligated to fix or take responsibility for other people's issues, even if they aren't involved."
    }
    },
    'Attachment': {
    'name': 'Attachment',
    'description': 'Compulsive attachment - pushing for quick commitment before solid connection',
    'scores': {
      0: "Emotional distance – Consistently maintains a cold, detached demeanor, avoiding emotional closeness, and showing little to no vulnerability or openness in the relationship. Avoidance of intimacy – Regularly pulls away from physical or emotional intimacy, resisting cuddling, deep conversations, or any form of closeness, even when their partner seeks connection.",
      2: "Frequent emotional withdrawal – Regularly distances themselves emotionally, particularly when the relationship requires emotional openness or vulnerability, leaving their partner feeling disconnected. Avoids emotional intimacy – Actively avoids deep, intimate conversations about feelings, fears, or relationship issues, brushing them off or changing the subject to avoid confrontation.",
      5: "Comfortable with intimacy: Easily forms close, trusting relationships and is open to emotional closeness without feeling overwhelmed or stifled. Balances independence and closeness: Maintains healthy boundaries in relationships, while also being open to giving and receiving support. Comfortable with conflict: Can handle disagreements or differences in a calm and constructive way, seeing them as a natural part of healthy relationships.",
      8: "Constantly seeks reassurance – Frequently asks their partner for reassurance about their love and commitment, feeling insecure even when reassured. Clinginess – Becomes overly dependent on their partner for emotional stability and often seeks constant closeness. Fear of abandonment – Worries excessively about their partner leaving, and may become distressed at the thought of being alone or rejected.",
      10: "Extreme need for constant reassurance – Continuously demands reassurances, even after being told multiple times that they are loved or valued, often making their partner feel exhausted by the frequent need for validation. Overwhelming clinginess – Unable to tolerate even short periods of separation, they may demand constant physical presence or communication, often suffocating their partner."
    }
  },
  'Boundaries': {
    'name': 'Boundaries',
    'description': 'Ability to set and maintain healthy personal boundaries',
    'scores': {
      0: "Overshares personal details immediately – Discloses deep trauma or inappropriate details to strangers. Touches people without consent – Ignores personal space, hugs or touches others despite discomfort. Forces intimacy in relationships – Assumes closeness without mutual development, calling someone their 'best friend' or 'soulmate' instantly.",
      2: "Frequently overshares – Discloses personal details too early or in inappropriate contexts. Has difficulty accepting 'no' – Pushes back when others set limits but eventually backs off. Interrupts personal space – Stands too close or touches casually without always noticing discomfort.",
      5: "Respecting their own limits: Clearly communicates when they need time for themselves or need to prioritize personal needs, without feeling guilty. Saying no when necessary: Is able to turn down requests or invitations that don't align with their values, goals, or current capacity. Being assertive without being aggressive: Expresses their needs, feelings, and opinions clearly and respectfully without dominating or allowing others to dominate them.",
      8: "Over-reliance on boundaries, leading to imbalances. Insistence on separate sleeping or intimate spaces. Avoids physical proximity. Avoids touch, even when welcomed. Rarely or never gives gifts. Unresponsive to your needs.",
      10: "Physically distant at all times – Avoids physical touch, even in appropriate situations. Sets extreme communication limits – Only responds to messages on their schedule, may require others to book time with them instead of spontaneous interaction. Keeps all aspects of life strictly separate – Rigidly divides work, friendships, family, and relationships, refusing to let them overlap."
    }
  },
  'Charm': {
    'name': 'Charm',
    'description': 'Over-the-top, disingenuous display of charisma to manipulate',
    'scores': {
      0: "Fails to make eye contact – Avoids looking at others, making interactions feel cold or disconnected. Monotone or dull speech – Speaks in a flat, emotionless, or robotic tone, making conversations unengaging. Lacks humor or playfulness – Does not joke, tease, or engage in lighthearted banter, making interactions feel heavy.",
      2: "Struggles with humor – Can joke occasionally but often misses timing or makes awkward comments. Mildly awkward body language – Slightly stiff posture, limited gestures, or an unnatural way of moving in social settings. Speaks in a straightforward or matter-of-fact tone – Lacks expressive variation but isn't completely robotic.",
      5: "Authentic and genuine: Uses charm in an authentic way, making others feel comfortable without trying to manipulate or alter their true self. Engages others without overpowering them: Can engage with others confidently but ensures that they don't dominate conversations or overwhelm others with attention.",
      8: "Quick-witted and smooth talker – Can easily make conversation, joke, and banter, but often keeps things surface-level. Effortlessly persuasive – Knows how to say the right thing to get people on their side, even if they don't fully mean it. Charismatic but noncommittal – Engages people easily but avoids deep personal investment.",
      10: "Over-the-top flattery – Gives exaggerated, excessive compliments that feel unnatural or manipulative. Mirrors personality and interests – Adopts the mannerisms, beliefs, or hobbies of others to seem like the 'perfect match.' Hyper-attentiveness – Makes people feel intensely special by focusing on them completely, but only as a tactic to gain trust."
    }
  },
  'Cognitive_Flexibility': {
    'name': 'Cognitive Flexibility',
    'description': 'Ability to adapt thinking and approach to different situations',
    'scores': {
      0: "Hyper-focus on precise meanings – Interprets language in a strict, literal sense, struggling with sarcasm, metaphors, or implied meanings due to a single-track focus on surface-level definitions. Intolerance of ambiguity – Becomes distressed or fixated when information is incomplete or vague, as their attention system demands clarity and fully formed concepts.",
      2: "Prefers clear and direct communication – Can handle some nuance but struggles when people are vague or indirect. Mild difficulty with sarcasm or jokes – May miss the joke at first but can understand it when explained. Likes consistency and predictability – Prefers routines and clear expectations but can adapt with effort.",
      5: "Healthy cognitive flexibility—demonstrates adaptability, flexibility, and resilience. Able to adjust to different situations appropriately.",
      8: "Believes in synchronicities – Sees meaningful coincidences in everyday life but doesn't rely on them to make major decisions. Trusts gut feelings over logic sometimes – Makes choices based on intuition but can acknowledge when evidence contradicts their instincts.",
      10: "Sees deep, hidden connections everywhere – Believes unrelated events or coincidences are meaningfully linked. Overinterprets personal significance – Believes everyday occurrences are messages meant specifically for them. Distorts cause and effect – Assumes thoughts, wishes, or rituals can directly influence reality."
    }
  },
  'Conflict': {
    'name': 'Conflict',
    'description': 'Prioritizing "winning" over understanding or resolving issues',
    'scores': {
      0: "Completely shuts down when confronted – Goes silent, refuses to speak, or physically leaves the conversation without resolution. Pretends conflict doesn't exist – Acts as if a disagreement never happened, even when directly addressed. Agrees with everyone, even if statements contradict each other – Will say 'yes' to opposing views just to avoid confrontation.",
      2: "Changes the subject when tension arises – Quickly redirects the conversation to avoid addressing the issue. Uses vague or unclear language – Speaks in a way that makes it hard to pin down their actual stance. Overuses softening phrases – Constantly adds 'I don't know, just my opinion' or 'I could be wrong' to avoid sounding too assertive.",
      5: "Frequently challenges others' opinions – Will debate ideas openly but doesn't necessarily escalate into personal attacks. Expresses disagreements bluntly – Tends to be direct and unfiltered rather than softening their words. Speaks in an authoritative or forceful manner – Comes across as intense or dominant in discussions.",
      8: "Constantly challenges others' opinions, even without reason, just to assert dominance. Uses blunt, harsh language without concern for others' feelings. Dominates conversations, often overpowering others' voices and ideas. Gets angry or condescending when others disagree or don't follow their logic.",
      10: "Escalates minor disagreements into violent outbursts, throwing things, shouting, or physically intimidating others to 'win' the argument. Uses threats of physical harm to control or scare others into agreeing with them or backing down in a conflict."
    }
  },
  'Control': {
    'name': 'Control',
    'description': 'Attempting to influence partner\'s actions, decisions, thoughts or emotions',
    'scores': {
      0: "Takes no initiative in decisions – Completely avoids making choices, even in situations that require leadership or direction. Has no personal preferences in relationships or work – Defers everything to others, refusing to express opinions or needs. Allows others to walk all over them – Never asserts themselves, even when faced with blatant mistreatment or unfairness.",
      2: "Avoids taking the lead unless absolutely necessary – Prefers others to make decisions but will step in if no one else does. Rarely asserts strong preferences – Goes along with group choices even if they don't fully agree. Struggles with setting firm expectations – Might express what they want but doesn't enforce it when pushed.",
      5: "Sets clear rules and consistently enforces expectations. Applies consistent consequences for inappropriate behavior. Corrects behavior without excessive punishment. Encourages accountability for actions and their impact. Monitors behavior without micromanaging.",
      8: "Expects others to follow their plans – Believes their way is best and pressures people to conform to their decisions. Dislikes when others act independently – Feels uneasy or resentful when people make decisions without consulting them. Uses guilt to influence others – Subtly pressures people by saying things like, 'After everything I've done for you...'",
      10: "Micromanages every aspect of others' lives – Dictates what people wear, eat, say, and do, leaving them no autonomy. Uses financial control to trap people – Lends money with strings attached, restricts access to resources, or forces dependence. Threatens severe consequences for disobedience – Uses intimidation, blackmail, or violence to maintain control."
    }
  },
  'Deception': {
    'name': 'Deception',
    'description': 'Intentionally misleading or misrepresenting truth to manipulate',
    'scores': {
      0: "Believes everything they're told at face value – Doesn't question information, no matter how unlikely or exaggerated it sounds. Falls for scams and deception repeatedly – Trusts strangers with personal information, money, or resources without hesitation. Takes sarcasm and jokes literally – Struggles to recognize when someone is being insincere or messing with them.",
      2: "Assumes people are honest by default – Tends to believe what others say unless given a strong reason to doubt. Rarely questions motives – Doesn't look for hidden agendas or manipulation in others' actions. Gives second (and third) chances too easily – Forgives quickly, even when someone has shown a pattern of dishonesty.",
      5: "Honest but tactful – Shares the truth while considering the feelings of others. Keeps confidences – Respects others' privacy and does not share sensitive information unless necessary. Transparent in intentions – Clearly communicates their motives without manipulation.",
      8: "Lies to avoid consequences – Regularly bends the truth to escape blame or get out of uncomfortable situations. Exaggerates achievements or status – Inflates accomplishments to impress others but doesn't completely fabricate them. Hides mistakes or failures – Covers up errors rather than admitting them openly.",
      10: "Fabricates an entirely false persona – Changes core aspects of their identity (background, values, personality) to manipulate different people. Leads a double life – Maintains multiple romantic relationships, families, or social identities without others knowing. Cheats compulsively – Engages in serial infidelity, often deceiving multiple partners at the same time."
    }
  },
  'Disrespect': {
    'name': 'Disrespect',
    'description': 'Verbal and non-verbal behaviors that devalue or undermine the other person',
    'scores': {
      0: "Never questions authority or decisions – Accepts whatever someone says without critique, even when it's unreasonable. Overly deferential in conversation – Allows others to dominate discussions, never interrupting or asserting their own perspective. Praises others excessively, even for bad ideas – Treats every opinion as valid, even when it's clearly flawed.",
      2: "Overly formal or deferential in casual settings – Uses excessive 'sir' or 'ma'am' or treats informal interactions too seriously. Over-apologizes for minor things – Says 'sorry' too often, even when no offense was given. Gives respect automatically rather than based on merit – Shows deference to people solely based on status or age rather than actions or character.",
      5: "Healthy disrespect—demonstrates adaptability, flexibility, and resilience. Able to adjust to different situations appropriately.",
      8: "Frequently interrupts but still listens when forced to – Talks over people but will acknowledge them if called out. Uses sarcasm or condescension often – Makes dismissive comments but isn't outright aggressive. Minimally engages in politeness – Says 'please' or 'thank you' only when it benefits them, not out of genuine respect.",
      10: "Openly disregards others' dignity – Shows no basic respect for people, treating them as inferior or unworthy of acknowledgment. Speaks to others in a tone of pure contempt – Uses a dismissive, sneering, or disgusted voice when addressing people. Deliberately refuses to acknowledge people's presence – Ignores greetings, introductions, or direct communication as a power move."
    }
  },
  'Dominance': {
    'name': 'Dominance',
    'description': 'Belief that power gives right to dictate others\' lives',
    'scores': {
      0: "Never disagrees with anyone, even when they should – Goes along with everything, even if it's harmful, unethical, or against their beliefs. Immediately defers to authority or stronger personalities – Lets others take charge in every situation, regardless of competence. Speaks in a hesitant, self-diminishing way – Uses phrases like 'I don't know,' 'Whatever you think,' or 'Sorry for asking' constantly.",
      2: "Prefers others to take the lead – Doesn't naturally seek control but will step up if absolutely necessary. Rarely pushes for their own way – Expresses preferences but backs down easily if met with resistance. Avoids making big decisions alone – Seeks input and reassurance before committing to choices.",
      5: "Leads by example – Inspires others through their actions rather than exerting control over them. Delegates responsibility – Trusts others to take ownership of tasks, empowering them to make decisions. Encourages collaboration – Fosters teamwork by valuing others' input and creating a sense of shared leadership.",
      8: "Prefers to be in charge whenever possible – Feels most comfortable making decisions and leading in group settings. Has a strong need for things to go their way – Pushes hard for their preferences but won't completely break relationships over it. Talks over or interrupts others frequently – Dominates conversations but still allows some input from others.",
      10: "Must always be in charge – Controls every decision, even in situations where they lack expertise or authority. Sees others as subordinates, not equals – Talks down to people and expects obedience rather than cooperation. Demands absolute compliance – Views disagreement as defiance and reacts aggressively to any pushback."
    }
  },
  'Dysregulation': {
    'name': 'Dysregulation',
    'description': 'Inability to manage and regulate emotional responses',
    'scores': {
      0: "Never expresses strong emotions, even in extreme situations – Appears unnaturally calm during crises, tragedies, or highly emotional moments. Forces logic over feelings in every situation – Dismisses emotions as irrelevant, always prioritizing rationality, even when emotional support is needed.",
      2: "Occasionally reacts impulsively in emotional situations – May blurt something out or show frustration but quickly regains control. Needs time to cool down after conflicts – Takes a bit longer than average to emotionally reset after disagreements or stress. Feels emotions intensely but doesn't always express them outwardly – Internally experiences strong feelings but manages to keep them contained.",
      5: "Expresses emotions appropriately – Can share feelings openly without suppressing or overreacting. Recovers quickly from emotional distress – Feels emotions deeply but can return to a calm state without getting stuck. Understands and 'name's emotions accurately – Recognizes what they're feeling and why, without confusion or denial.",
      8: "Has noticeable mood swings but can recover with effort – Emotions shift quickly, but they can sometimes regain composure after a while. Occasionally lashes out in frustration or anger – Struggles to contain emotions, leading to heated arguments or impulsive remarks. Tends to overreact to stress but recognizes it later – May get overwhelmed and make a scene, then regret it afterward.",
      10: "Rapid and extreme mood swings – Goes from happy to enraged or devastated within minutes, often over minor triggers. Frequent emotional outbursts – Yells, cries, or lashes out impulsively, struggling to contain strong emotions. Takes everything personally – Sees neutral or even well-intended comments as attacks and reacts defensively."
    }
  },
  'Emotional_Overexposure': {
    'name': 'Emotional Overexposure',
    'description': 'Revealing personal emotions or experiences too soon or too intensely',
    'scores': {
      0: "Never shares personal struggles or emotions – Keeps all difficulties private, even from close friends and family. Refuses to ask for help, even when needed – Would rather suffer in silence than admit they need assistance. Avoids deep or personal conversations – Keeps interactions superficial and steers discussions away from emotions.",
      2: "Shares personal thoughts sparingly – Opens up only in very controlled, rare situations. Struggles to express emotions clearly – May acknowledge feelings but keeps 'description's vague or detached. Prefers to handle problems alone – Will rarely ask for help but might accept it if strongly encouraged.",
      5: "Comfortably expresses emotions when needed – Can share feelings of sadness, joy, frustration, or excitement without fear. Asks for help when necessary – Recognizes when they need support and seeks it from trusted people. Admits personal mistakes and takes responsibility – Openly acknowledges errors without excessive shame or defensiveness.",
      8: "Shares emotions intensely and frequently – Regularly talks about deep feelings, even in casual or professional settings. Has difficulty keeping emotional experiences private – Finds it unnatural to hold back feelings, even when it might be more appropriate to do so.",
      10: "Overshares personal trauma with strangers or acquaintances – Reveals deeply personal or tragic details to people they barely know. Uses emotional distress to control situations – Breaks down in tears or acts devastated to manipulate others into compliance."
    }
  },
  'Empathy': {
    'name': 'Empathy',
    'description': 'Concern or sensitivity toward feelings and needs of others',
    'scores': {
      0: "Feels no remorse for harming others – Can lie, manipulate, or hurt people without guilt or second thoughts. Lacks emotional reaction to others' suffering – Feels nothing when witnessing pain, grief, or distress, even in close relationships. Sees people as tools to be used – Views relationships as transactional, only engaging with others for personal benefit.",
      2: "Understands emotions intellectually but doesn't feel them deeply – Knows when someone is upset but doesn't experience much emotional resonance. Gives surface-level sympathy without real emotional investment – Says things like 'That sucks' or 'Sorry to hear that' without genuine concern.",
      5: "Active listening – Gives full attention, makes eye contact, and responds thoughtfully when others share their feelings. Emotional recognition – Accurately identifies emotions in others based on tone, body language, and words. Perspective-taking – Can imagine how someone else feels and understand their point of view, even if they disagree.",
      8: "Takes on others' emotions as their own – Feels deep distress when others are upset, sometimes even more than the person experiencing the issue. Struggles to set emotional boundaries – Absorbs the pain of others and has difficulty separating their own feelings from someone else's.",
      10: "Physically and emotionally incapacitated by others' suffering – Becomes so overwhelmed by another person's emotions that they cannot function in their daily life. Loses all sense of self in relationships – Merges identities with others, feeling their emotions as if they were their own to the point of personal identity erosion."
    }
  },
  'Enmeshment': {
    'name': 'Enmeshment',
    'description': 'Viewing privacy as negative, wanting no boundaries between partners',
    'scores': {
      0: "Feels no emotional connection to others, even family or close friends – Interactions feel mechanical rather than meaningful. Struggles to form deep relationships – May have acquaintances or surface-level social interactions but lacks true intimacy.",
      2: "Keeps relationships at a surface level – Engages in social interactions but avoids deep emotional closeness. Struggles to express emotions openly – Feels discomfort discussing personal feelings, even with close people.",
      5: "Shares emotions appropriately – Expresses feelings openly with trusted people without oversharing or suppressing. Balances independence with connection – Enjoys emotional closeness but doesn't rely on others to regulate their emotions.",
      8: "Overly involved in their partner's emotions – Feels deeply affected by their partner's mood and struggles to separate their own feelings from theirs. Wants constant emotional closeness – Feels uneasy or rejected if their partner needs time alone or personal space.",
      10: "Believes that one person is their 'other half' – Feels incomplete without their partner and sees them as the only source of happiness. Expects total emotional and mental synchronization – Believes a 'true soulmate' should always understand their feelings and thoughts without needing communication."
    }
  },
  'Exploitation': {
    'name': 'Exploitation',
    'description': 'Taking advantage of partner for personal gain',
    'scores': {
      0: "Allows others to make decisions for them – Lets people dictate what they should do, where they should go, or how they should spend their time. Feels obligated to comply with any request – Experiences intense guilt or fear at the idea of disappointing someone, even a stranger.",
      2: "Has trouble saying no but occasionally does – Feels guilty refusing requests but will push back in extreme situations. Often overextends themselves to help others – Frequently takes on too much responsibility, though sometimes realizes it later.",
      5: "Knows when to say yes and when to say no – Helps others generously but also sets limits when needed. Recognizes and expects fair exchanges – Gives time and effort but also expects and accepts reciprocity in relationships.",
      8: "Uses weaponized incompetence to avoid responsibilities – Pretends to be bad at chores, parenting, or work tasks so that others pick up the slack. Plays dumb when it benefits them – Feigns confusion or lack of knowledge in situations where responsibility or effort would be required.",
      10: "Treats people as financial assets – Uses others for money, fraud, or labor without fair compensation. Weaponizes emotions to get what they want – Fakes vulnerability, guilt-trips, or fabricates crises to manipulate others into doing their bidding."
    }
  },
  'Grandiosity': {
    'name': 'Grandiosity',
    'description': 'Sense of entitlement, believing they deserve special treatment',
    'scores': {
      0: "Feels inherently unworthy – Believes they have no value, talent, or significance, no matter how much evidence suggests otherwise. Downplays or denies personal achievements – Dismisses compliments, insists their successes were luck, or credits others instead of themselves.",
      2: "Struggles with self-confidence in many areas – Often doubts their abilities but can occasionally recognize their strengths. Downplays achievements but accepts some credit – May say things like, 'It wasn't a big deal,' but won't outright reject compliments.",
      5: "Acknowledges accomplishments without bragging – Can confidently say, 'I worked hard for this,' without needing excessive praise. Comfortable with both success and failure – Sees mistakes as learning opportunities and doesn't let setbacks define them.",
      8: "Always compares themselves to others – Feels the need to establish that they are more successful, intelligent, or talented. Subtly one-ups people in conversation – If someone shares an achievement, they respond with a bigger or better one.",
      10: "Believes they are a once-in-a-generation genius or historical figure. Sees themselves as infallible; failure is always someone else's fault. Talks about their destined greatness as if it's already fact."
    }
  },
  'Impulsivity': {
    'name': 'Impulsivity',
    'description': 'Acting without thinking through consequences',
    'scores': {
      0: "Overthinks every decision, no matter how small. Requires extensive planning before taking any action. Avoids spontaneity to the point of missing opportunities.",
      2: "Overthinks before making even minor decisions. Struggles with last-minute changes and spontaneity. Finds it difficult to take action without extensive planning.",
      5: "Can make quick decisions when needed but doesn't act recklessly. Enjoys spontaneity but balances it with planning. Takes calculated risks without being reckless.",
      8: "Frequently makes spontaneous decisions without much thought. Often spends money irresponsibly but avoids total financial ruin. Changes plans frequently, sometimes frustrating others.",
      10: "Acts on urges instantly without considering consequences. Frequently changes plans, jobs, or relationships on a whim. Engages in dangerous behaviors (reckless driving, substance abuse, etc.)."
    }
  },
  'Inconsistency': {
    'name': 'Inconsistency',
    'description': 'Unpredictable or erratic behavior in actions, words, or availability',
    'scores': {
      0: "Follows strict routines and rituals with no flexibility. Becomes extremely distressed when plans change, even slightly. Repeats the same behaviors, meals, or daily habits for years without deviation.",
      2: "Prefers strict routines but can adjust with effort. Double-checks work or tasks obsessively but eventually moves on. Dislikes last-minute changes but won't completely shut down over them.",
      5: "Follows through on commitments and responsibilities. Maintains steady progress toward long-term goals. Balances routine with flexibility when needed.",
      8: "Frequently changes plans but sometimes sticks to commitments. Starts projects with enthusiasm but struggles to finish them. Forgets obligations occasionally, requiring reminders.",
      10: "Contradicts themselves within the same conversation – Makes conflicting statements minutes apart without acknowledging the contradiction. Invents entirely new personal beliefs on the spot – Constructs arguments or philosophies in real time with no connection to past views."
    }
  },
  'Intensity': {
    'name': 'Intensity',
    'description': 'Extreme emotional experiences that can overwhelm both partners',
    'scores': {
      0: "Lacks strong opinions or convictions about anything. Rarely shows enthusiasm, excitement, or deep emotions. Speaks in a monotone voice with little variation in expression.",
      2: "Rarely gets excited or passionate about things but can show mild interest. Speaks in a calm, subdued tone with minimal expression. Prefers low-stimulation activities and avoids high-energy environments.",
      5: "Shows enthusiasm for things they care about but doesn't overwhelm others. Can focus deeply on tasks without becoming obsessive. Expresses emotions openly but in a controlled and appropriate way.",
      8: "Over-reliance on intensity, leading to imbalances. Frequent, overwhelming communication. You feel numb. Fast-paced relationship progression. Sudden grand gestures (e.g., expensive gifts, big plans).",
      10: "Falls in love instantly and obsessively – Believes in soulmates, quickly attaching themselves to others and expecting immediate emotional intimacy and commitment. Engages in love-bombing – Overwhelms the person with excessive affection, gifts, compliments, and attention in a very short time."
    }
  },
  'Isolation': {
    'name': 'Isolation',
    'description': 'Limiting or controlling partner\'s access to friends, family, or support',
    'scores': {
      0: "Family members or friends are constantly over – Has little to no private time, with family or friends frequently dropping by uninvited or staying for long periods. Never has a moment alone – Struggles to find personal time, always surrounded by others, even when they want to be by themselves.",
      2: "Always has someone around – Has family, friends, or roommates constantly in their space, rarely spending time alone. Shares personal issues openly – Talks about their problems with anyone who will listen, often oversharing in casual conversations.",
      5: "Enjoys alone time but also socializes regularly. Shares personal details with close friends but keeps some things private. Takes time for self-care or hobbies without feeling isolated.",
      8: "Over-reliance on isolation, leading to imbalances. Consistently suggests they join you at gatherings, framing it as 'being supportive' or 'wanting to spend time together'. Social proof can be manipulated to make you feel as if you are 'different' or 'out of step' with a perceived majority.",
      10: "Constant Monitoring: Tracking phone, texts, social media, or location without consent. Limiting Social Interactions: Discouraging or forbidding time with family, friends, or colleagues. Emotional Manipulation: Making the partner feel guilty for socializing or playing the victim."
    }
  },
  'Neediness': {
    'name': 'Neediness',
    'description': 'Relying excessively on partner for emotional stability and security',
    'scores': {
      0: "Refuses All Help, Even in Crisis: Even in urgent or life-threatening situations, they absolutely refuse any help, insisting on handling everything alone, no matter the cost to their health or well-being.",
      2: "Refuses Help: Consistently rejects any offers of help, even when it's clearly needed. Overcompensates: Takes on excessive tasks or responsibilities alone to prove they don't need anyone.",
      5: "Healthy neediness—demonstrates adaptability, flexibility, and resilience. Able to adjust to different situations appropriately.",
      8: "Over-reliance on neediness, leading to imbalances. Sends multiple messages per day and seeks immediate responses. Expects to spend nearly all free time together. Relies on you for all decisions, even minor ones.",
      10: "Frequent Need for Validation: Regularly seeks reassurance or approval from others, but is not overly dramatic about it. Discomfort with Alone Time: Often feels uneasy or lonely when by themselves and looks for company or someone to talk to."
    }
  },
  'Perseveration': {
    'name': 'Perseveration',
    'description': 'Persistently repeating or focusing on thoughts/behaviors when no longer productive',
    'scores': {
      0: "Constantly Abandoning Projects: Starts numerous tasks or projects, but never finishes any, leaving them incomplete and forgotten. Shifting Focus Without Completing Anything: Frequently shifts attention from one interest to another, with no intention or ability to follow through on the current focus.",
      2: "Frequently Starts Projects but Struggles to Complete Them: Often begins new tasks or hobbies but rarely finishes them, leaving many things in progress but few completed. Frequently Shifts Focus: Has a tendency to lose interest in ongoing projects or goals.",
      5: "Healthy perseveration—demonstrates adaptability, flexibility, and resilience. Able to adjust to different situations appropriately.",
      8: "Ruminating on Past Events: Often revisits and replays past events, conversations, or mistakes, overthinking them and struggling to let them go. Inflexible in Approach: Sticks rigidly to one way of thinking or doing things, even when it's not the most effective or efficient method.",
      10: "Obsessive Pursuit of Unhealthy Goals: Continually chasing goals, people, or objects that are clearly harmful or unattainable, refusing to accept failure or moving on despite clear signs that it's damaging. Stalking or Harassing Others: Constantly following, monitoring, or contacting someone, even after they have expressed disinterest or asked for space."
    }
  },
  'Sensation_seeking': {
    'name': 'Sensation-seeking',
    'description': 'Seeking out new physical experiences, novel sensations, or exciting adventures',
    'scores': {
      0: "Can't handle minor changes without melting down. Lives in a total bubble of rigid control. Experiences even joy or excitement as threatening.",
      2: "Avoids new experiences or environments — insists on familiar restaurants, routines, and people. Rarely initiates fun or spontaneous activities and often resists when others suggest them.",
      5: "Embracing New Experiences: Willing to try new activities, like visiting new places, trying new foods, or exploring new hobbies, but also knows when to stop if things become too overwhelming.",
      8: "Over-reliance on sensation-seeking, leading to imbalances. Constantly changes friend groups, avoids deeper connections in favor of fresh ones. Needs constant stimulation to feel engaged, may create drama for excitement.",
      10: "Chronic Escaping from Reality: Obsessively pursues extreme experiences, using travel, substances, or dangerous activities as a way to escape any form of stability or routine. Repeated Engagement in High-Risk Activities: Consistently engages in highly dangerous, life-threatening activities."
    }
  },
  'Sense_of_Self': {
    'name': 'Sense of Self',
    'description': 'Understanding and integration of own identity, values, beliefs, and behaviors',
    'scores': {
      0: "No Regard for Right or Wrong: Makes decisions purely based on personal gain, with no consideration of ethics, consequences, or harm to others. Deceptive and Manipulative: Lies, deceives, and manipulates people for personal gain without feeling any remorse or ethical conflict.",
      2: "Self-Awareness: Regularly reflects on their thoughts, emotions, and actions, maintaining a clear understanding of their strengths, weaknesses, values, and goals. Consistent Core Values: Demonstrates a strong set of personal values and principles.",
      5: "Strong Personal Beliefs: Holds firm personal beliefs and values, but is open to listening to other perspectives. Consistent Identity: Maintains a clear sense of who they are and what they stand for.",
      8: "Insists on presenting a consistent self-image, regardless of the situation. Resists changing their identity in response to new experiences or feedback. Struggles to understand or accept how others view them.",
      10: "Inflexible Beliefs: Holds their views and beliefs as absolute, refusing to consider alternative perspectives or new information. Over-Identification with Labels: Strongly identifies with specific labels or categories and becomes defensive when these are challenged."
    }
  },
  'Superficiality': {
    'name': 'Superficiality',
    'description': 'Focus on external appearances or surface-level interactions',
    'scores': {
      0: "Avoids all superficial interactions, completely disregarding small talk, even when it's necessary for social cohesion. Is consumed by intense, abstract conversations and refuses to engage in anything perceived as trivial or shallow.",
      2: "Focuses intensely on meaningful conversations and avoids small talk or shallow topics. Seeks out deep, philosophical discussions, often ignoring lighter social interactions.",
      5: "Comfortable engaging in small talk when appropriate, understanding its role in building rapport and easing into deeper conversations. Values meaningful discussions but also enjoys light-hearted, casual interactions.",
      8: "Obsesses over appearances in all areas of life, including their own, others, and their environment, prioritizing how things look over what they actually are. Engages in conversations solely about superficial topics like status, material possessions, or shallow opinions.",
      10: "Obsesses over appearances in all areas of life, including their own, others, and their environment, prioritizing how things look over what they actually are. Engages in conversations solely about superficial topics like status, material possessions, or shallow opinions."
    }
  },
  'Trust': {
    'name': 'Trust',
    'description': 'Ability to rely on and believe in others',
    'scores': {
      0: "Constantly questions the motives of everyone around them, believing that others are always scheming against them or trying to manipulate them, even without any evidence. Assumes betrayal is inevitable, frequently preparing for the worst.",
      2: "Doubts others' motives constantly, assuming ulterior agendas in even the simplest interactions. Keeps emotional distance from others, rarely opening up or revealing their true feelings.",
      5: "Gives others the benefit of the doubt, trusting people unless given a reason to question their integrity. Opens up emotionally, sharing personal thoughts and feelings in appropriate contexts.",
      8: "Over-reliance on trust, leading to imbalances. Quickly takes advice or follows others without verification. Overly optimistic. Shares personal information freely, even with strangers.",
      10: "Believes everything people say, without any skepticism or need for verification, assuming that others are always truthful. Trusts people indiscriminately, extending full trust to anyone, regardless of their history or behavior."
    }
  },
  'Unorthodoxy': {
    'name': 'Unorthodoxy',
    'description': 'Actions or beliefs that challenge conventional social norms',
    'scores': {
      0: "Refuses to consider alternative perspectives, dismissing any differing opinions or viewpoints as wrong, irrelevant, or dangerous. Rigidly adheres to traditions or rules, no matter how outdated or impractical they may be.",
      2: "Respects traditions and established systems, but is open to revisiting them and evolving them when necessary for improvement or progress. Follows established rules and norms, but adapts them in a way that makes sense in varying contexts.",
      5: "Healthy unorthodoxy—demonstrates adaptability, flexibility, and resilience. Able to adjust to different situations appropriately.",
      8: "Constantly challenges societal norms and frequently dismisses conventional wisdom, often suggesting that widely accepted ideas are flawed or outdated. Deliberately rejects established systems and rules, choosing alternative methods or lifestyles.",
      10: "Forces radical and harmful behaviors onto others, such as encouraging extreme acts of rebellion or violence against societal norms without considering the harm caused. Promotes a lifestyle of constant disruption."
    }
  },
  'Validation_seeking': {
    'name': 'Validation-seeking',
    'description': 'Constantly seeking reassurance or approval to feel worthy',
    'scores': {
      0: "Ignores positive feedback: Actively disregards compliments or recognition, either by dismissing them or acting indifferent. Resists acknowledgment: Refuses to accept or acknowledge praise or approval, even when it is deserved or warranted.",
      2: "Avoids seeking feedback: Rarely asks for feedback or validation, even in situations where it would help improve or clarify their work or decisions. Downplays achievements: Minimizes or ignores their successes, not wanting or expecting praise or acknowledgment from others.",
      5: "Accepts compliments gracefully: Responds to praise with humility, acknowledging the positive feedback without dismissing it or seeking more. Seeks reassurance in a balanced way: Asks for feedback or guidance when needed, but doesn't over-rely on others to confirm their self-worth.",
      8: "Frequently seeks approval: Regularly looks for validation from others, especially in important decisions or personal achievements. Overemphasizes praise: Places significant weight on receiving compliments or positive feedback and feels motivated by it.",
      10: "Constantly seeks approval: Frequently asks others for reassurance or validation, even when it's unnecessary or inappropriate. Overly reliant on compliments: Becomes emotionally dependent on receiving praise, using it as the primary source of self-worth."
    }
  }

}

# ========================== PLAYER TYPES ==========================
PLAYER_TYPES = {
    'puppet_master': {
        'name': 'The Puppet Master',
        'nickname': 'Manipulative Morgan',
        'oldname': 'Emotional Predator (Psychopath)',
        'description': 'Skilled at emotional manipulation and psychological control',
        'highTraits': ['Exploitation', 'Deception', 'Charm'],
        'lowTraits': ['Sense_of_Self', 'Attachment', 'Accountability'],
        'emotionsCaused': ['uneasy', 'confused', 'guilty']
    },
    'intimidator': {
        'name': 'The Intimidator',
        'nickname': 'Menacing Marley',
        'oldname': 'The Terrorist',
        'description': 'Uses fear and aggression to maintain control',
        'highTraits': ['Control', 'Boundaries', 'Dominance'],
        'lowTraits': ['Empathy', 'Accountability', 'Neediness'],
        'emotionsCaused': ['afraid', 'violated', 'powerless']
    },
    'self_obsessed': {
        'name': 'The Self-Obsessed',
        'nickname': 'Egocentric Evan',
        'oldname': 'The Narcissist',
        'description': 'Everything revolves around their needs and image',
        'highTraits': ['Grandiosity', 'Validation_seeking', 'Superficiality'],
        'lowTraits': ['Trust', 'Empathy', 'Accountability'],
        'emotionsCaused': ['unworthy', 'confused', 'ashamed']
    },
    'drill_sergeant': {
        'name': 'The Drill Sergeant',
        'nickname': 'Domineering Devin',
        'oldname': 'The Drill Sergeant (Lundy Bancroft)',
        'description': 'Rigid, controlling, and demanding compliance',
        'highTraits': ['Control', 'Dominance', 'Sense_of_Self'],
        'lowTraits': ['Neediness', 'Emotional_Overexposure', 'Unorthodoxy'],
        'emotionsCaused': ['tense', 'suffocated', 'deflated']
  },
    'suspicious_strategist': {
    'name': 'The Suspicious Strategist',
    'nickname': 'Conspiratorial Corey',
    'oldname': 'The Paranoid',
    'description': 'Paranoid and controlling, sees threats everywhere',
    'highTraits': ['Isolation', 'Conflict', 'Control'],
    'lowTraits': ['Trust', 'Charm', 'Cognitive_Flexibility'],
    'emotionsCaused': ['disoriented', 'apprehensive', 'isolated']
  },
    'master_of_everything': {
    'name': 'Master of Everything',
    'nickname': 'Arrogant Avery',
    'oldname': 'Mr. Always Right (Lundy Bancroft)',
    'description': 'Always right, never wrong, knows everything',
    'highTraits': ['Dominance', 'Conflict', 'Grandiosity'],
    'lowTraits': ['Enmeshment', 'Neediness', 'Accountability'],
    'emotionsCaused': ['drained', 'insecure', 'resigned']
  },
    'subtle_saboteur': {
    'name': 'The Subtle Saboteur',
    'nickname': 'Backhanded Blake',
    'oldname': 'Passive Aggressive Man',
    'description': 'Passive-aggressive manipulation and undermining',
    'highTraits': ['Disrespect', 'Inconsistency', 'Control'],
    'lowTraits': ['Dysregulation', 'Conflict', 'Accountability'],
    'emotionsCaused': ['confused', 'dismissed', 'resentful']
  },
    'clinger': {
    'name': 'The Clinger',
    'nickname': 'Needy Noel',
    'oldname': 'The Clinger (Sandra L. Brown)',
    'description': 'Smothering attachment and emotional dependency',
    'highTraits': ['Enmeshment', 'Dysregulation', 'Attachment'],
    'lowTraits': ['Sense_of_Self', 'Disrespect', 'Grandiosity'],
    'emotionsCaused': ['smothered', 'guilty', 'trapped']
  },
    'addict': {
    'name': 'The Addict',
    'nickname': 'Adrenaline Ainsley',
    'oldname': 'The Addict',
    'description': 'Addictive behaviors affecting relationship stability',
    'highTraits': ['Dysregulation', 'Impulsivity', 'Inconsistency'],
    'lowTraits': ['Sense_of_Self', 'Control', 'Accountability'],
    'emotionsCaused': ['hypervigilant', 'overwhelmed', 'guilty']
  },
    'parental_seeker': {
    'name': 'The Parental Seeker',
    'nickname': 'Dependent Drew',
    'oldname': 'The Mommy Seeker (Sandra L. Brown)',
    'description': 'Seeks partner to be their parent figure',
    'highTraits': ['Neediness', 'Charm', 'Attachment'],
    'lowTraits': ['Dominance', 'Perseveration', 'Accountability'],
    'emotionsCaused': ['overwhelmed', 'lonely', 'resentful']
  },
    'future_faker': {
    'name': 'The Future Faker',
    'nickname': 'Storytelling Sam',
    'oldname': 'The Future Faker (Nathalie Lue)',
    'description': 'Makes promises about future they never intend to keep',
    'highTraits': ['Deception', 'Inconsistency', 'Superficiality'],
    'lowTraits': ['Attachment', 'Perseveration', 'Empathy'],
    'emotionsCaused': ['disillusioned', 'betrayed', 'insecure']
  },
    'freewheeler': {
    'name': 'The Freewheeler',
    'nickname': 'Tornado Toby',
    'oldname': 'ADHD Man',
    'description': 'Chaotic, impulsive, ADHD-like behavior patterns',
    'highTraits': ['Impulsivity', 'Unorthodoxy', 'Sensation_seeking'],
    'lowTraits': ['Control', 'Dominance', 'Cognitive_Flexibility'],
    'emotionsCaused': ['overwhelmed', 'unseen', 'resentful']
  },
    'thinker': {
    'name': 'The Thinker',
    'nickname': 'Blunt Bailey',
    'oldname': 'Autistic Man',
    'description': 'Logical, analytical, potentially autistic traits',
    'highTraits': ['Cognitive_Flexibility', 'Perseveration', 'Trust'],
    'lowTraits': ['Impulsivity', 'Charm', 'Sensation_seeking'],
    'emotionsCaused': ['lonely', 'rejected', 'misunderstood']
  },
    'emotional_invalidator': {
    'name': 'Emotional Invalidator',
    'nickname': 'Neglectful Nico',
    'oldname': 'Emotional Invalidator (Lundy Bancroft)',
    'description': 'Dismisses and invalidates partner\'s emotions',
    'highTraits': ['Disrespect', 'Grandiosity', 'Dominance'],
    'lowTraits': ['Enmeshment', 'Attachment', 'Empathy'],
    'emotionsCaused': ['invalidated', 'lonely', 'unworthy']
  },
    'emotionally_distant': {
    'name': 'The Emotionally Distant',
    'nickname': 'Avoidant Alex',
    'oldname': 'Mr. Unavailable (Nathalie Lue)',
    'description': 'Avoids emotional intimacy and connection',
    'highTraits': ['Inconsistency', 'Superficiality', 'Control'],
    'lowTraits': ['Enmeshment', 'Dysregulation', 'Attachment'],
    'emotionsCaused': ['neglected', 'confused', 'abandoned']
  },
    'rake': {
    'name': 'The Rake',
    'nickname': 'Charming Charlie',
    'oldname': 'The Rake',
    'description': 'Seductive charmer who pursues then abandons',
    'highTraits': ['Charm', 'Sensation_seeking', 'Intensity'],
    'lowTraits': ['Attachment', 'Accountability', 'Sense_of_Self'],
    'emotionsCaused': ['desire', 'confusion', 'despair']
  },
    'perpetual_victim': {
    'name': 'The Perpetual Victim',
    'nickname': 'Pity-party Parker',
    'oldname': 'The Perpetual Victim (Lundy Bancroft)',
    'description': 'Always the victim, never takes responsibility',
    'highTraits': ['Validation_seeking', 'Inconsistency', 'Emotional_Overexposure'],
    'lowTraits': ['Accountability', 'Empathy', 'Perseveration'],
    'emotionsCaused': ['guilty', 'drained', 'frustrated']
  },
    'no_red_flags': {
    'name': 'No Significant Red Flags',
    'nickname': 'Healthy Henry',
    'oldname': 'Healthy Individual',
    'description': 'Communication patterns appear healthy and respectful',
    'highTraits': [],
    'lowTraits': [],
    'emotionsCaused': ['secure', 'respected', 'valued']
    }
}

RELATIONSHIP_DIMENSIONS = {
    "RESPECT": ["Empathy", "Disrespect", "Trust", "Boundaries", "Isolation"],
    "SAFETY": ["Conflict", "Dominance", "Control", "Accountability", "Dysregulation"],
    "TRUST": ["Deception", "Superficiality", "Inconsistency", "Sense_of_Self", "Charm"],
    "CONNECTION": ["Enmeshment", "Attachment", "Neediness", "Intensity", "Validation_seeking"],
    "MATURITY": ["Impulsivity", "Emotional_Overexposure", "Perseveration", "Grandiosity", "Validation_seeking"],
    "FAIRNESS": ["Accountability", "Exploitation", "Cognitive_Flexibility", "Unorthodoxy", "Sensation_seeking"]
}

# ========================== RELATIONSHIP TYPES ==========================
RELATIONSHIP_TYPES = [
    {'value': 'romantic-partner', 'label': '💕 Romantic Partner'},
    {'value': 'dating', 'label': '🌹 Dating'},
    {'value': 'spouse', 'label': '💍 Spouse/Married'},
    {'value': 'friend', 'label': '👥 Friend'},
    {'value': 'family-member', 'label': '👨‍👩‍👧‍👦 Family Member'},
    {'value': 'coworker', 'label': '💼 Coworker'},
    {'value': 'other', 'label': '🤷‍♀️ Other'}
]

# ========================== DURATION OPTIONS ==========================
DURATION_OPTIONS = [
    {'value': 'less-than-month', 'label': 'Less than a month'},
    {'value': '1-6-months', 'label': '1-6 months'},
    {'value': '6-months-1-year', 'label': '6 months - 1 year'},
    {'value': '1-2-years', 'label': '1-2 years'},
    {'value': '2-5-years', 'label': '2-5 years'},
    {'value': 'more-than-5-years', 'label': 'More than 5 years'}
]

# ========================== SCORING & HELPER FUNCTIONS ==========================

def get_trait_score(trait_name, score):
    trait = UNES_TRAITS.get(trait_name)
    if not trait or score not in trait['scores']:
        return None
    return trait['scores'][score]

def get_all_trait_names():
    return list(UNES_TRAITS.keys())

def get_all_player_types():
    return list(PLAYER_TYPES.keys())

def get_player_types_by_pattern(pattern):
    result = []
    for key, player in PLAYER_TYPES.items():
        if pattern == 'concerning' and key != 'no_red_flags':
            result.append({'key': key, **player})
        elif pattern == 'healthy' and key == 'no_red_flags':
            result.append({'key': key, **player})
        elif pattern not in ['concerning', 'healthy']:
            result.append({'key': key, **player})
    return result

def generate_trait_prompt(trait_name):
    trait = UNES_TRAITS.get(trait_name)
    if not trait:
        return ''
    return f"""
{trait['name']} ({trait['description']}):
- Score 0: {trait['scores'][0]}
- Score 2: {trait['scores'][2]}
- Score 5: {trait['scores'][5]} (DEFAULT - balanced/healthy)
- Score 8: {trait['scores'][8]}
- Score 10: {trait['scores'][10]}
"""

def generate_complete_analysis_prompt():
    return '\n'.join([generate_trait_prompt(trait) for trait in UNES_TRAITS])

def get_default_trait_scores():
    return {trait: 5 for trait in UNES_TRAITS}

