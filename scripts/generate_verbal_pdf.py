#!/usr/bin/env python3
"""
Generate Verbal Ability PDF for TCS NQT Preparation
Contains 150+ questions across 8 major topics
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.pdf_generator import TCSNQTPDFGenerator


def build_reading_comprehension(pdf, start_q):
    """Reading Comprehension - 5 passages, ~25 questions"""
    q = start_q
    pdf.add_topic_header(
        "Section 1: Reading Comprehension",
        "Read each passage carefully and answer the questions that follow. "
        "These passages test your ability to understand main ideas, draw inferences, "
        "identify tone, and interpret vocabulary in context."
    )

    # ---- Passage 1: Technology ----
    pdf.add_subtopic_header("Passage 1 - Artificial Intelligence in Healthcare")
    pdf.add_text(
        "Artificial intelligence is rapidly transforming the healthcare industry, offering "
        "unprecedented opportunities for early diagnosis, personalized treatment, and operational "
        "efficiency. Machine learning algorithms can now analyze medical images with accuracy that "
        "rivals, and in some cases surpasses, that of experienced radiologists. AI-powered tools are "
        "being deployed to predict patient deterioration in intensive care units, enabling timely "
        "interventions that save lives. Furthermore, natural language processing is streamlining "
        "clinical documentation, freeing physicians to spend more time with patients. However, the "
        "integration of AI into medicine raises significant ethical concerns. Issues of data privacy, "
        "algorithmic bias, and the potential displacement of healthcare workers must be addressed "
        "thoughtfully. Regulatory frameworks are still catching up with the pace of technological "
        "advancement, and the lack of transparency in many AI models — often called the 'black box' "
        "problem — makes it difficult for clinicians to trust and validate AI-generated recommendations. "
        "Striking the right balance between innovation and patient safety remains a formidable challenge.",
        style='Normal'
    )
    questions = [
        {
            "text": "What is the primary purpose of the passage?",
            "options": {
                "A": "To argue that AI should replace doctors entirely",
                "B": "To discuss the benefits and challenges of AI in healthcare",
                "C": "To explain how machine learning algorithms work",
                "D": "To criticize the healthcare industry for slow adoption of AI"
            },
            "answer": "B) To discuss the benefits and challenges of AI in healthcare",
            "explanation": "The passage presents both the advantages (early diagnosis, efficiency) and challenges (ethics, bias, regulation) of AI in healthcare.",
            "difficulty": "Easy"
        },
        {
            "text": "What does the term 'black box' problem refer to in the passage?",
            "options": {
                "A": "The high cost of AI systems in hospitals",
                "B": "The lack of transparency in how AI models arrive at their conclusions",
                "C": "The physical appearance of AI hardware",
                "D": "The difficulty of transporting AI equipment"
            },
            "answer": "B) The lack of transparency in how AI models arrive at their conclusions",
            "explanation": "The passage explicitly states that the 'black box' problem refers to the lack of transparency in many AI models, making it difficult for clinicians to trust AI recommendations.",
            "difficulty": "Easy"
        },
        {
            "text": "Which of the following is NOT mentioned as a benefit of AI in healthcare?",
            "options": {
                "A": "Personalized treatment plans",
                "B": "Reduced cost of medical insurance",
                "C": "Early diagnosis of diseases",
                "D": "Streamlining clinical documentation"
            },
            "answer": "B) Reduced cost of medical insurance",
            "explanation": "The passage mentions early diagnosis, personalized treatment, operational efficiency, and streamlined documentation but does not mention reduced insurance costs.",
            "difficulty": "Medium"
        },
        {
            "text": "The tone of the passage can best be described as:",
            "options": {
                "A": "Overwhelmingly optimistic",
                "B": "Harshly critical",
                "C": "Balanced and analytical",
                "D": "Indifferent and detached"
            },
            "answer": "C) Balanced and analytical",
            "explanation": "The author presents both positives and negatives of AI in healthcare without showing extreme bias, maintaining an analytical perspective throughout.",
            "difficulty": "Medium"
        },
        {
            "text": "The word 'formidable' as used in the passage most nearly means:",
            "options": {
                "A": "Simple",
                "B": "Inspiring fear or dread",
                "C": "Impressively difficult",
                "D": "Completely impossible"
            },
            "answer": "C) Impressively difficult",
            "explanation": "In this context, 'formidable' means something that is intimidatingly challenging — striking the right balance is a significant, difficult task.",
            "difficulty": "Medium"
        },
    ]
    for qdata in questions:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    pdf.add_page_break()

    # ---- Passage 2: Environment ----
    pdf.add_subtopic_header("Passage 2 - Ocean Plastic Pollution")
    pdf.add_text(
        "The world's oceans are drowning in plastic. Every year, approximately eight million metric "
        "tons of plastic waste enter marine environments, endangering ecosystems and threatening human "
        "health. Microplastics — tiny fragments less than five millimeters in diameter — have been "
        "found in the deepest ocean trenches and even in Arctic sea ice. Marine animals, from plankton "
        "to whales, ingest these particles, leading to internal injuries, starvation, and death. The "
        "problem extends to humans through the seafood supply chain, as microplastics accumulate in "
        "the tissues of fish and shellfish. International efforts to combat plastic pollution have "
        "gained momentum. Several nations have banned single-use plastics, and innovative cleanup "
        "technologies, such as ocean barriers and autonomous collection vessels, are being tested. "
        "Yet experts warn that cleanup alone is insufficient. Without addressing the root cause — "
        "the overproduction and overconsumption of disposable plastics — the problem will continue "
        "to escalate. A circular economy model, where materials are reused and recycled rather than "
        "discarded, offers the most sustainable long-term solution.",
        style='Normal'
    )
    questions = [
        {
            "text": "According to the passage, how much plastic enters the oceans annually?",
            "options": {
                "A": "Five million metric tons",
                "B": "Eight million metric tons",
                "C": "Ten million metric tons",
                "D": "Twelve million metric tons"
            },
            "answer": "B) Eight million metric tons",
            "explanation": "The passage explicitly states 'approximately eight million metric tons of plastic waste enter marine environments' each year.",
            "difficulty": "Easy"
        },
        {
            "text": "What does the passage suggest is the most effective long-term solution to plastic pollution?",
            "options": {
                "A": "Banning all types of plastic globally",
                "B": "Deploying autonomous collection vessels",
                "C": "Adopting a circular economy model",
                "D": "Reducing seafood consumption"
            },
            "answer": "C) Adopting a circular economy model",
            "explanation": "The passage concludes by stating that a circular economy model, where materials are reused and recycled, 'offers the most sustainable long-term solution.'",
            "difficulty": "Medium"
        },
        {
            "text": "The word 'escalate' as used in the passage most nearly means:",
            "options": {
                "A": "Decrease gradually",
                "B": "Remain unchanged",
                "C": "Increase rapidly in intensity",
                "D": "Become more visible"
            },
            "answer": "C) Increase rapidly in intensity",
            "explanation": "'Escalate' means to increase or intensify. The passage warns the problem will continue to grow worse without addressing root causes.",
            "difficulty": "Easy"
        },
        {
            "text": "Why does the author mention microplastics found in Arctic sea ice?",
            "options": {
                "A": "To show that pollution is limited to cold regions",
                "B": "To emphasize the pervasive and far-reaching nature of plastic pollution",
                "C": "To argue that the Arctic needs special protection",
                "D": "To demonstrate that microplastics are harmless in cold environments"
            },
            "answer": "B) To emphasize the pervasive and far-reaching nature of plastic pollution",
            "explanation": "By mentioning the deepest ocean trenches and Arctic ice, the author illustrates that plastic contamination has reached even the most remote corners of the planet.",
            "difficulty": "Medium"
        },
        {
            "text": "Which of the following can be inferred from the passage?",
            "options": {
                "A": "Ocean cleanup technologies have successfully eliminated most plastic waste",
                "B": "Humans are immune to the effects of microplastic contamination",
                "C": "Reducing plastic production is more important than cleanup efforts alone",
                "D": "All nations have agreed to ban single-use plastics"
            },
            "answer": "C) Reducing plastic production is more important than cleanup efforts alone",
            "explanation": "The passage states that 'cleanup alone is insufficient' and that addressing overproduction and overconsumption is essential, implying prevention outweighs remediation.",
            "difficulty": "Medium"
        },
    ]
    for qdata in questions:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    pdf.add_page_break()

    # ---- Passage 3: Business ----
    pdf.add_subtopic_header("Passage 3 - The Gig Economy")
    pdf.add_text(
        "The gig economy has fundamentally altered the landscape of employment worldwide. Platforms "
        "like Uber, Freelancer, and TaskRabbit have enabled millions of workers to earn income on "
        "their own terms, choosing when, where, and how much they work. For many, this flexibility "
        "is liberating, offering an escape from rigid corporate structures and long commutes. Young "
        "professionals, in particular, are drawn to gig work as it allows them to pursue diverse "
        "projects and develop a broad skill set. However, the gig economy has a darker side that is "
        "often overlooked. Gig workers typically lack access to benefits that traditional employees "
        "take for granted: health insurance, retirement plans, paid leave, and job security. The "
        "absence of a minimum wage guarantee means that many gig workers earn below the poverty line "
        "after accounting for expenses. Critics argue that companies profit enormously from this model "
        "while shifting financial risk onto individual workers. Governments around the world are now "
        "grappling with how to regulate this sector, attempting to protect worker rights without "
        "stifling the innovation that makes gig platforms attractive.",
        style='Normal'
    )
    questions = [
        {
            "text": "What is the author's attitude toward the gig economy?",
            "options": {
                "A": "Completely supportive",
                "B": "Entirely negative",
                "C": "Nuanced, acknowledging both advantages and drawbacks",
                "D": "Dismissive and uninterested"
            },
            "answer": "C) Nuanced, acknowledging both advantages and drawbacks",
            "explanation": "The passage discusses both the flexibility and liberation of gig work and its drawbacks such as lack of benefits and low wages, presenting a balanced view.",
            "difficulty": "Easy"
        },
        {
            "text": "According to the passage, which of the following is a concern about gig workers?",
            "options": {
                "A": "They have too much job security",
                "B": "They earn excessively high wages",
                "C": "They lack access to health insurance and retirement plans",
                "D": "They are required to work fixed hours"
            },
            "answer": "C) They lack access to health insurance and retirement plans",
            "explanation": "The passage explicitly mentions that gig workers 'typically lack access to benefits' including health insurance and retirement plans.",
            "difficulty": "Easy"
        },
        {
            "text": "The phrase 'shifting financial risk onto individual workers' implies that:",
            "options": {
                "A": "Workers invest in the company's stock",
                "B": "Companies avoid bearing costs and liabilities that workers must absorb",
                "C": "Workers receive higher pay to compensate for risks",
                "D": "Companies share profits equally with workers"
            },
            "answer": "B) Companies avoid bearing costs and liabilities that workers must absorb",
            "explanation": "The phrase means that companies transfer the burden of expenses (insurance, equipment, taxes) to individual workers rather than bearing these costs themselves.",
            "difficulty": "Medium"
        },
        {
            "text": "Why are young professionals particularly attracted to gig work?",
            "options": {
                "A": "It guarantees a high salary",
                "B": "It offers diverse projects and helps develop a broad skill set",
                "C": "It provides comprehensive health benefits",
                "D": "It requires no skills or qualifications"
            },
            "answer": "B) It offers diverse projects and helps develop a broad skill set",
            "explanation": "The passage states that young professionals are drawn to gig work because 'it allows them to pursue diverse projects and develop a broad skill set.'",
            "difficulty": "Easy"
        },
        {
            "text": "What challenge do governments face regarding the gig economy?",
            "options": {
                "A": "How to completely eliminate gig work",
                "B": "How to force all workers into traditional employment",
                "C": "How to protect worker rights without stifling innovation",
                "D": "How to increase taxes on gig workers"
            },
            "answer": "C) How to protect worker rights without stifling innovation",
            "explanation": "The passage concludes by stating governments are 'attempting to protect worker rights without stifling the innovation that makes gig platforms attractive.'",
            "difficulty": "Medium"
        },
    ]
    for qdata in questions:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    pdf.add_page_break()

    # ---- Passage 4: Science ----
    pdf.add_subtopic_header("Passage 4 - CRISPR Gene Editing")
    pdf.add_text(
        "CRISPR-Cas9, a revolutionary gene-editing technology, has opened new frontiers in biology "
        "and medicine. Originally discovered as a bacterial defense mechanism against viruses, CRISPR "
        "allows scientists to precisely cut and modify DNA sequences with remarkable accuracy and "
        "efficiency. This technology holds immense promise for treating genetic disorders such as "
        "sickle cell disease, cystic fibrosis, and certain forms of cancer. Clinical trials are "
        "already underway, and early results have been encouraging. Beyond medicine, CRISPR has "
        "applications in agriculture, where it can create crop varieties that are more resistant to "
        "drought, pests, and disease, potentially addressing food security challenges in developing "
        "nations. However, the power of CRISPR also raises profound ethical questions. The possibility "
        "of editing human embryos to create so-called 'designer babies' has alarmed ethicists and "
        "policymakers alike. In 2018, a Chinese scientist controversially claimed to have created the "
        "first gene-edited babies, an act widely condemned by the scientific community. The incident "
        "underscored the urgent need for international guidelines governing the use of this powerful "
        "technology.",
        style='Normal'
    )
    questions = [
        {
            "text": "What was CRISPR-Cas9 originally discovered as?",
            "options": {
                "A": "A tool for agricultural improvement",
                "B": "A method for creating designer babies",
                "C": "A bacterial defense mechanism against viruses",
                "D": "A cancer treatment technique"
            },
            "answer": "C) A bacterial defense mechanism against viruses",
            "explanation": "The passage states it was 'originally discovered as a bacterial defense mechanism against viruses.'",
            "difficulty": "Easy"
        },
        {
            "text": "Which of the following best describes the author's view of CRISPR technology?",
            "options": {
                "A": "It is entirely beneficial with no drawbacks",
                "B": "It is too dangerous and should be banned",
                "C": "It is promising but requires careful ethical oversight",
                "D": "It is overhyped and unlikely to succeed"
            },
            "answer": "C) It is promising but requires careful ethical oversight",
            "explanation": "The author describes CRISPR's benefits in medicine and agriculture but also highlights ethical concerns and the need for international guidelines.",
            "difficulty": "Medium"
        },
        {
            "text": "Why was the 2018 incident involving gene-edited babies significant?",
            "options": {
                "A": "It proved that CRISPR is completely safe",
                "B": "It demonstrated the need for international regulations on gene editing",
                "C": "It showed that gene editing has no medical applications",
                "D": "It led to the immediate banning of CRISPR worldwide"
            },
            "answer": "B) It demonstrated the need for international regulations on gene editing",
            "explanation": "The passage says the incident 'underscored the urgent need for international guidelines governing the use of this powerful technology.'",
            "difficulty": "Medium"
        },
        {
            "text": "The word 'profound' as used in the passage most nearly means:",
            "options": {
                "A": "Shallow and insignificant",
                "B": "Very deep or intense",
                "C": "Amusing and entertaining",
                "D": "Temporary and fleeting"
            },
            "answer": "B) Very deep or intense",
            "explanation": "'Profound' means very great or intense. The ethical questions raised by CRISPR are deep and serious in nature.",
            "difficulty": "Easy"
        },
        {
            "text": "How can CRISPR potentially address food security challenges?",
            "options": {
                "A": "By reducing the global population",
                "B": "By creating crop varieties resistant to drought, pests, and disease",
                "C": "By replacing all natural crops with synthetic food",
                "D": "By eliminating the need for agriculture altogether"
            },
            "answer": "B) By creating crop varieties resistant to drought, pests, and disease",
            "explanation": "The passage mentions CRISPR can 'create crop varieties that are more resistant to drought, pests, and disease.'",
            "difficulty": "Easy"
        },
    ]
    for qdata in questions:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    pdf.add_page_break()

    # ---- Passage 5: Social Science ----
    pdf.add_subtopic_header("Passage 5 - The Psychology of Decision-Making")
    pdf.add_text(
        "Human decision-making is far less rational than most people assume. Decades of research in "
        "behavioral psychology and economics have revealed that our choices are heavily influenced by "
        "cognitive biases — systematic patterns of deviation from rationality. One of the most "
        "well-documented biases is the anchoring effect, where people rely too heavily on the first "
        "piece of information they encounter when making decisions. For example, a shopper who sees "
        "a shirt originally priced at five thousand rupees marked down to two thousand perceives it "
        "as a bargain, even if the shirt is objectively worth only one thousand. Similarly, the "
        "availability heuristic causes people to overestimate the likelihood of events that are easily "
        "recalled, such as plane crashes, while underestimating more common risks like heart disease. "
        "Confirmation bias — the tendency to seek information that supports one's pre-existing beliefs "
        "while ignoring contradictory evidence — is perhaps the most pervasive of all. Understanding "
        "these biases is crucial not only for individuals seeking to make better decisions but also for "
        "organizations designing policies, marketing strategies, and user interfaces that account for "
        "predictable human irrationality.",
        style='Normal'
    )
    questions = [
        {
            "text": "What is the main argument of the passage?",
            "options": {
                "A": "Humans are perfectly rational decision-makers",
                "B": "Cognitive biases systematically distort human decision-making",
                "C": "Marketing strategies are always unethical",
                "D": "Plane crashes are more common than heart disease"
            },
            "answer": "B) Cognitive biases systematically distort human decision-making",
            "explanation": "The passage's central theme is that human decision-making is influenced by systematic cognitive biases that deviate from rationality.",
            "difficulty": "Easy"
        },
        {
            "text": "The example of the marked-down shirt illustrates which cognitive bias?",
            "options": {
                "A": "Confirmation bias",
                "B": "Availability heuristic",
                "C": "Anchoring effect",
                "D": "Hindsight bias"
            },
            "answer": "C) Anchoring effect",
            "explanation": "The shirt example shows how the original price (the anchor) makes the discounted price seem like a bargain, illustrating the anchoring effect.",
            "difficulty": "Easy"
        },
        {
            "text": "According to the passage, why do people overestimate the likelihood of plane crashes?",
            "options": {
                "A": "Because plane crashes are actually very common",
                "B": "Because of the anchoring effect",
                "C": "Because plane crash reports are easily recalled due to media coverage",
                "D": "Because of confirmation bias"
            },
            "answer": "C) Because plane crash reports are easily recalled due to media coverage",
            "explanation": "The availability heuristic causes people to overestimate events that are 'easily recalled' — plane crashes receive extensive media coverage, making them more memorable.",
            "difficulty": "Medium"
        },
        {
            "text": "The word 'pervasive' as used in the passage most nearly means:",
            "options": {
                "A": "Rare and unusual",
                "B": "Spreading widely throughout",
                "C": "Easily correctable",
                "D": "Limited in scope"
            },
            "answer": "B) Spreading widely throughout",
            "explanation": "'Pervasive' means widespread or existing everywhere. Confirmation bias is described as the most widespread of all biases.",
            "difficulty": "Medium"
        },
        {
            "text": "Why is understanding cognitive biases important for organizations?",
            "options": {
                "A": "To exploit consumers more effectively",
                "B": "To design policies and interfaces that account for predictable human behavior",
                "C": "To eliminate all forms of marketing",
                "D": "To make employees less productive"
            },
            "answer": "B) To design policies and interfaces that account for predictable human behavior",
            "explanation": "The passage states that understanding biases is crucial for organizations 'designing policies, marketing strategies, and user interfaces that account for predictable human irrationality.'",
            "difficulty": "Medium"
        },
    ]
    for qdata in questions:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    return q


def build_grammar(pdf, start_q):
    """Grammar - 20 questions on tenses, articles, prepositions, subject-verb agreement"""
    q = start_q
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 2: Grammar",
        "Choose the correct option that makes the sentence grammatically correct. "
        "Topics covered: tenses, articles, prepositions, subject-verb agreement, and more."
    )

    questions = [
        # Tenses
        {
            "text": "She ______ for two hours before the guests arrived.",
            "options": {"A": "has been cooking", "B": "had been cooking", "C": "was cooking", "D": "cooked"},
            "answer": "B) had been cooking",
            "explanation": "The past perfect continuous tense ('had been cooking') is used to describe an action that was ongoing before another past action ('arrived').",
            "difficulty": "Medium"
        },
        {
            "text": "By the time the project is completed, we ______ on it for over a year.",
            "options": {"A": "will work", "B": "will have been working", "C": "are working", "D": "have worked"},
            "answer": "B) will have been working",
            "explanation": "The future perfect continuous tense is used to describe an action that will have been ongoing up to a point in the future.",
            "difficulty": "Hard"
        },
        {
            "text": "The train ______ by the time we reach the station.",
            "options": {"A": "will leave", "B": "has left", "C": "will have left", "D": "leaves"},
            "answer": "C) will have left",
            "explanation": "The future perfect tense ('will have left') indicates an action that will be completed before another future event.",
            "difficulty": "Medium"
        },
        {
            "text": "I wish I ______ harder during my college years.",
            "options": {"A": "study", "B": "studied", "C": "had studied", "D": "have studied"},
            "answer": "C) had studied",
            "explanation": "'Wish' followed by past perfect ('had studied') expresses regret about a past action that cannot be changed.",
            "difficulty": "Medium"
        },
        {
            "text": "The company ______ its new product next Monday.",
            "options": {"A": "is launching", "B": "launched", "C": "has launched", "D": "was launching"},
            "answer": "A) is launching",
            "explanation": "The present continuous tense can be used for planned future events. 'Next Monday' confirms a scheduled future action.",
            "difficulty": "Easy"
        },
        # Articles
        {
            "text": "______ honest person is always respected in society.",
            "options": {"A": "A", "B": "An", "C": "The", "D": "No article needed"},
            "answer": "B) An",
            "explanation": "'Honest' begins with a vowel sound (the 'h' is silent), so the article 'an' is used.",
            "difficulty": "Easy"
        },
        {
            "text": "He is ______ best player on the team.",
            "options": {"A": "a", "B": "an", "C": "the", "D": "no article needed"},
            "answer": "C) the",
            "explanation": "The definite article 'the' is used with superlatives ('the best') to indicate the highest degree.",
            "difficulty": "Easy"
        },
        {
            "text": "______ Ganges is considered sacred by millions of people.",
            "options": {"A": "A", "B": "An", "C": "The", "D": "No article needed"},
            "answer": "C) The",
            "explanation": "The definite article 'the' is used before the names of rivers, oceans, and mountain ranges.",
            "difficulty": "Easy"
        },
        # Prepositions
        {
            "text": "She has been absent ______ class for three consecutive days.",
            "options": {"A": "in", "B": "from", "C": "at", "D": "for"},
            "answer": "B) from",
            "explanation": "The correct preposition with 'absent' is 'from.' One is absent from a place or event.",
            "difficulty": "Easy"
        },
        {
            "text": "The manager insisted ______ completing the report before the deadline.",
            "options": {"A": "at", "B": "for", "C": "on", "D": "with"},
            "answer": "C) on",
            "explanation": "'Insist' is followed by the preposition 'on.' 'Insisted on' means to demand firmly.",
            "difficulty": "Medium"
        },
        {
            "text": "He is good ______ mathematics but weak ______ English.",
            "options": {"A": "in, at", "B": "at, in", "C": "at, at", "D": "in, in"},
            "answer": "B) at, in",
            "explanation": "'Good at' and 'weak in' are the correct prepositional phrases used with these adjectives.",
            "difficulty": "Medium"
        },
        {
            "text": "The thief broke ______ the house through the back window.",
            "options": {"A": "in", "B": "into", "C": "on", "D": "through"},
            "answer": "B) into",
            "explanation": "'Broke into' is the correct phrasal verb meaning to enter a building illegally by force.",
            "difficulty": "Easy"
        },
        # Subject-Verb Agreement
        {
            "text": "Neither the teacher nor the students ______ aware of the schedule change.",
            "options": {"A": "was", "B": "were", "C": "is", "D": "has been"},
            "answer": "B) were",
            "explanation": "With 'neither...nor,' the verb agrees with the subject closest to it. 'Students' is plural, so 'were' is correct.",
            "difficulty": "Medium"
        },
        {
            "text": "Each of the participants ______ given a certificate after the workshop.",
            "options": {"A": "were", "B": "was", "C": "are", "D": "have been"},
            "answer": "B) was",
            "explanation": "'Each' is a singular indefinite pronoun, so it takes a singular verb 'was.'",
            "difficulty": "Medium"
        },
        {
            "text": "The committee ______ divided in their opinions on the new policy.",
            "options": {"A": "was", "B": "were", "C": "is", "D": "are"},
            "answer": "B) were",
            "explanation": "When a collective noun refers to individual members acting separately (divided opinions), a plural verb is used.",
            "difficulty": "Hard"
        },
        {
            "text": "A number of students ______ absent from the lecture yesterday.",
            "options": {"A": "was", "B": "were", "C": "is", "D": "has been"},
            "answer": "B) were",
            "explanation": "'A number of' takes a plural verb because it means 'many.' (Contrast with 'the number of,' which is singular.)",
            "difficulty": "Medium"
        },
        # Mixed Grammar
        {
            "text": "If I ______ you, I would not accept that offer.",
            "options": {"A": "am", "B": "was", "C": "were", "D": "be"},
            "answer": "C) were",
            "explanation": "In the second conditional (hypothetical present), the subjunctive mood requires 'were' for all subjects, including 'I.'",
            "difficulty": "Medium"
        },
        {
            "text": "The news ______ very disturbing; everyone was shocked.",
            "options": {"A": "were", "B": "was", "C": "are", "D": "have been"},
            "answer": "B) was",
            "explanation": "'News' is an uncountable noun and always takes a singular verb, despite ending in 's.'",
            "difficulty": "Easy"
        },
        {
            "text": "Hardly had the meeting begun ______ the fire alarm went off.",
            "options": {"A": "than", "B": "when", "C": "then", "D": "before"},
            "answer": "B) when",
            "explanation": "'Hardly...when' is a fixed correlative conjunction pair used to describe two events in quick succession.",
            "difficulty": "Medium"
        },
        {
            "text": "No sooner did he finish his presentation ______ the audience burst into applause.",
            "options": {"A": "when", "B": "than", "C": "then", "D": "that"},
            "answer": "B) than",
            "explanation": "'No sooner...than' is the correct correlative conjunction pair. It indicates one event followed immediately by another.",
            "difficulty": "Medium"
        },
    ]

    for qdata in questions:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    return q


def build_vocabulary(pdf, start_q):
    """Vocabulary - 20 questions"""
    q = start_q
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 3: Vocabulary",
        "Test your knowledge of word meanings, usage, and contextual understanding. "
        "Choose the option that best fits the meaning or context."
    )

    questions = [
        {
            "text": "Choose the word that best fits the meaning: 'To make something less severe or intense.'",
            "options": {"A": "Aggravate", "B": "Mitigate", "C": "Instigate", "D": "Fabricate"},
            "answer": "B) Mitigate",
            "explanation": "'Mitigate' means to make less severe, serious, or painful. 'Aggravate' means the opposite.",
            "difficulty": "Medium"
        },
        {
            "text": "The word 'ubiquitous' means:",
            "options": {"A": "Rare and hard to find", "B": "Present everywhere at the same time", "C": "Extremely dangerous", "D": "Slow and methodical"},
            "answer": "B) Present everywhere at the same time",
            "explanation": "'Ubiquitous' means found everywhere or seemingly present everywhere. Example: 'Smartphones have become ubiquitous.'",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the word that means 'a person who leads a simple life and avoids physical pleasures.'",
            "options": {"A": "Hedonist", "B": "Ascetic", "C": "Philanthropist", "D": "Pragmatist"},
            "answer": "B) Ascetic",
            "explanation": "An 'ascetic' practices severe self-discipline and abstains from indulgence. A 'hedonist' is the opposite — someone who pursues pleasure.",
            "difficulty": "Medium"
        },
        {
            "text": "The word 'ephemeral' is closest in meaning to:",
            "options": {"A": "Eternal", "B": "Short-lived", "C": "Mysterious", "D": "Powerful"},
            "answer": "B) Short-lived",
            "explanation": "'Ephemeral' means lasting for a very short time. Example: 'The beauty of cherry blossoms is ephemeral.'",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the correct meaning of the word 'pragmatic':",
            "options": {"A": "Idealistic and impractical", "B": "Dealing with things sensibly and realistically", "C": "Overly emotional", "D": "Extremely stubborn"},
            "answer": "B) Dealing with things sensibly and realistically",
            "explanation": "'Pragmatic' means focused on practical results rather than theory or ideology.",
            "difficulty": "Easy"
        },
        {
            "text": "What does 'gregarious' mean?",
            "options": {"A": "Fond of company; sociable", "B": "Preferring to be alone", "C": "Aggressive and hostile", "D": "Extremely cautious"},
            "answer": "A) Fond of company; sociable",
            "explanation": "'Gregarious' describes someone who is sociable and enjoys the company of others.",
            "difficulty": "Medium"
        },
        {
            "text": "The word 'ameliorate' means:",
            "options": {"A": "To make worse", "B": "To make better or improve", "C": "To destroy completely", "D": "To postpone indefinitely"},
            "answer": "B) To make better or improve",
            "explanation": "'Ameliorate' means to make something bad or unsatisfactory better. Example: 'Steps were taken to ameliorate working conditions.'",
            "difficulty": "Hard"
        },
        {
            "text": "Which word means 'a strong supporter of a party, cause, or person'?",
            "options": {"A": "Adversary", "B": "Partisan", "C": "Mediator", "D": "Skeptic"},
            "answer": "B) Partisan",
            "explanation": "A 'partisan' is a strong, often uncritical supporter. An 'adversary' is an opponent.",
            "difficulty": "Medium"
        },
        {
            "text": "The word 'lethargic' describes someone who is:",
            "options": {"A": "Energetic and enthusiastic", "B": "Sluggish and lacking energy", "C": "Angry and irritable", "D": "Calm and composed"},
            "answer": "B) Sluggish and lacking energy",
            "explanation": "'Lethargic' means affected by lethargy — a lack of energy and enthusiasm.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the word that means 'to officially prohibit something':",
            "options": {"A": "Endorse", "B": "Sanction", "C": "Proscribe", "D": "Advocate"},
            "answer": "C) Proscribe",
            "explanation": "'Proscribe' means to forbid or prohibit. Note: 'prescribe' (to recommend) is different from 'proscribe' (to forbid).",
            "difficulty": "Hard"
        },
        {
            "text": "The word 'candid' means:",
            "options": {"A": "Secretive and deceptive", "B": "Truthful and straightforward", "C": "Indecisive and wavering", "D": "Formal and reserved"},
            "answer": "B) Truthful and straightforward",
            "explanation": "'Candid' means frank and honest. A candid person speaks openly without hiding the truth.",
            "difficulty": "Easy"
        },
        {
            "text": "What does the word 'exacerbate' mean?",
            "options": {"A": "To resolve a conflict", "B": "To make a problem or situation worse", "C": "To celebrate with great joy", "D": "To examine carefully"},
            "answer": "B) To make a problem or situation worse",
            "explanation": "'Exacerbate' means to make something already bad even worse. Example: 'The drought exacerbated the food shortage.'",
            "difficulty": "Medium"
        },
        {
            "text": "The word 'benevolent' describes someone who is:",
            "options": {"A": "Cruel and malicious", "B": "Well-meaning and kindly", "C": "Indifferent and apathetic", "D": "Ambitious and competitive"},
            "answer": "B) Well-meaning and kindly",
            "explanation": "'Benevolent' means well-meaning and kind. It comes from Latin 'bene' (well) and 'volent' (wishing).",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the correct meaning of 'garrulous':",
            "options": {"A": "Extremely quiet", "B": "Excessively talkative", "C": "Physically strong", "D": "Emotionally sensitive"},
            "answer": "B) Excessively talkative",
            "explanation": "'Garrulous' means excessively talkative, especially on trivial matters. Synonyms include loquacious and verbose.",
            "difficulty": "Hard"
        },
        {
            "text": "What does 'equivocal' mean?",
            "options": {"A": "Clear and unambiguous", "B": "Open to more than one interpretation; ambiguous", "C": "Extremely loud", "D": "Completely false"},
            "answer": "B) Open to more than one interpretation; ambiguous",
            "explanation": "'Equivocal' means ambiguous or open to multiple interpretations. The prefix 'equi-' means equal, suggesting equal validity of different interpretations.",
            "difficulty": "Hard"
        },
        {
            "text": "The word 'tenacious' means:",
            "options": {"A": "Easily giving up", "B": "Holding firmly to something; persistent", "C": "Extremely fragile", "D": "Superficially attractive"},
            "answer": "B) Holding firmly to something; persistent",
            "explanation": "'Tenacious' means persistent and determined. A tenacious person does not easily give up.",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the word that means 'happening by chance rather than design':",
            "options": {"A": "Deliberate", "B": "Fortuitous", "C": "Inevitable", "D": "Predictable"},
            "answer": "B) Fortuitous",
            "explanation": "'Fortuitous' means happening by accident or chance. It is often confused with 'fortunate,' but they have different meanings.",
            "difficulty": "Hard"
        },
        {
            "text": "The word 'reticent' describes a person who is:",
            "options": {"A": "Outspoken and bold", "B": "Reserved and unwilling to speak freely", "C": "Cheerful and optimistic", "D": "Careless and reckless"},
            "answer": "B) Reserved and unwilling to speak freely",
            "explanation": "'Reticent' means not revealing one's thoughts or feelings readily. A reticent person prefers to keep things to themselves.",
            "difficulty": "Medium"
        },
        {
            "text": "What does the word 'cogent' mean?",
            "options": {"A": "Weak and unconvincing", "B": "Clear, logical, and convincing", "C": "Confusing and complex", "D": "Emotional and passionate"},
            "answer": "B) Clear, logical, and convincing",
            "explanation": "'Cogent' means clear, logical, and persuasive. A cogent argument is one that is well-reasoned and compelling.",
            "difficulty": "Hard"
        },
        {
            "text": "The word 'sycophant' refers to:",
            "options": {"A": "A person who gives honest feedback", "B": "A person who flatters others to gain advantage", "C": "A person who avoids social interaction", "D": "A person who solves disputes"},
            "answer": "B) A person who flatters others to gain advantage",
            "explanation": "A 'sycophant' is a person who acts obsequiously toward someone important to gain advantage. Also called a 'yes-man' or 'toady.'",
            "difficulty": "Medium"
        },
    ]

    for qdata in questions:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    return q


def build_sentence_correction(pdf, start_q):
    """Sentence Correction - 20 questions"""
    q = start_q
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 4: Sentence Correction",
        "Identify the error in the sentence and choose the correct version. "
        "Focus on common grammatical mistakes including subject-verb agreement, "
        "pronoun errors, misplaced modifiers, parallelism, and word usage."
    )

    questions = [
        {
            "text": "Identify the correct sentence:",
            "options": {
                "A": "Each of the boys have completed their assignment.",
                "B": "Each of the boys has completed his assignment.",
                "C": "Each of the boys have completed his assignment.",
                "D": "Each of the boys has completed their assignments."
            },
            "answer": "B) Each of the boys has completed his assignment.",
            "explanation": "'Each' is singular and requires the singular verb 'has' and singular pronoun 'his.'",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the grammatically correct sentence:",
            "options": {
                "A": "The data shows that the experiment was successful.",
                "B": "The data show that the experiment was successful.",
                "C": "The datas show that the experiment was successful.",
                "D": "The data showing that the experiment was successful."
            },
            "answer": "B) The data show that the experiment was successful.",
            "explanation": "'Data' is the plural of 'datum,' so it takes the plural verb 'show' in formal usage.",
            "difficulty": "Medium"
        },
        {
            "text": "Identify the correct sentence:",
            "options": {
                "A": "Running quickly down the street, the bus was missed by him.",
                "B": "Running quickly down the street, he missed the bus.",
                "C": "The bus was missed by him, running quickly down the street.",
                "D": "He missed the bus, quickly running down the street was he."
            },
            "answer": "B) Running quickly down the street, he missed the bus.",
            "explanation": "A participial phrase at the beginning of a sentence must refer to the subject. 'He' (not 'the bus') was running.",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the correct sentence:",
            "options": {
                "A": "Between you and I, the proposal needs more work.",
                "B": "Between you and me, the proposal needs more work.",
                "C": "Between you and myself, the proposal needs more work.",
                "D": "Between I and you, the proposal needs more work."
            },
            "answer": "B) Between you and me, the proposal needs more work.",
            "explanation": "'Between' is a preposition and requires the objective case pronoun 'me,' not the subjective 'I' or reflexive 'myself.'",
            "difficulty": "Easy"
        },
        {
            "text": "Which sentence is correct?",
            "options": {
                "A": "She is more taller than her sister.",
                "B": "She is taller than her sister.",
                "C": "She is most taller than her sister.",
                "D": "She is tallest than her sister."
            },
            "answer": "B) She is taller than her sister.",
            "explanation": "Comparative adjectives like 'taller' should not be preceded by 'more' or 'most.' These are used only with multi-syllable adjectives.",
            "difficulty": "Easy"
        },
        {
            "text": "Identify the error: 'The team, along with their coach, were celebrating the victory.'",
            "options": {
                "A": "Replace 'their' with 'its'",
                "B": "Replace 'were' with 'was'",
                "C": "Replace 'along with' with 'and'",
                "D": "No error"
            },
            "answer": "B) Replace 'were' with 'was'",
            "explanation": "The subject is 'the team' (singular). Phrases like 'along with' do not change the number of the subject. The verb should be singular: 'was celebrating.'",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the correct sentence:",
            "options": {
                "A": "He not only plays cricket but also football.",
                "B": "He plays not only cricket but also football.",
                "C": "Not only he plays cricket but also football.",
                "D": "He plays cricket not only but also football."
            },
            "answer": "B) He plays not only cricket but also football.",
            "explanation": "The correlative conjunctions 'not only...but also' must be placed directly before the parallel elements they connect ('cricket' and 'football').",
            "difficulty": "Medium"
        },
        {
            "text": "Identify the correct sentence:",
            "options": {
                "A": "The reason for his absence is because he is ill.",
                "B": "The reason for his absence is that he is ill.",
                "C": "The reason for his absence is due to he is ill.",
                "D": "The reason for his absence is since he is ill."
            },
            "answer": "B) The reason for his absence is that he is ill.",
            "explanation": "'Reason...is that' is the correct construction. 'Reason...is because' is redundant since 'reason' already implies 'because.'",
            "difficulty": "Medium"
        },
        {
            "text": "Which sentence is grammatically correct?",
            "options": {
                "A": "Everyone should bring their own lunch.",
                "B": "Everyone should bring his or her own lunch.",
                "C": "Everyone should bring our own lunch.",
                "D": "Everyone should bring its own lunch."
            },
            "answer": "B) Everyone should bring his or her own lunch.",
            "explanation": "In formal grammar, 'everyone' is singular and requires the singular pronoun 'his or her.' (Note: 'their' is increasingly accepted in informal usage.)",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the correct sentence:",
            "options": {
                "A": "I would have went to the party if I had known about it.",
                "B": "I would have gone to the party if I had known about it.",
                "C": "I would have go to the party if I had known about it.",
                "D": "I would have going to the party if I had known about it."
            },
            "answer": "B) I would have gone to the party if I had known about it.",
            "explanation": "After 'would have,' the past participle 'gone' is required, not the simple past 'went.'",
            "difficulty": "Easy"
        },
        {
            "text": "Identify the error: 'Despite of the heavy rain, the match continued.'",
            "options": {
                "A": "Replace 'Despite of' with 'Despite'",
                "B": "Replace 'heavy' with 'heavily'",
                "C": "Replace 'continued' with 'was continued'",
                "D": "No error"
            },
            "answer": "A) Replace 'Despite of' with 'Despite'",
            "explanation": "'Despite' is never followed by 'of.' The correct usage is 'Despite the rain' or 'In spite of the rain.'",
            "difficulty": "Easy"
        },
        {
            "text": "Which sentence uses the correct word?",
            "options": {
                "A": "The new policy will effect all employees.",
                "B": "The new policy will affect all employees.",
                "C": "The new policy will affective all employees.",
                "D": "The new policy will effective all employees."
            },
            "answer": "B) The new policy will affect all employees.",
            "explanation": "'Affect' is a verb meaning to influence. 'Effect' is typically a noun meaning result. Here, a verb is needed.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the correct sentence:",
            "options": {
                "A": "Whom do you think is the best candidate?",
                "B": "Who do you think is the best candidate?",
                "C": "Whose do you think is the best candidate?",
                "D": "Which do you think is the best candidate?"
            },
            "answer": "B) Who do you think is the best candidate?",
            "explanation": "'Who' is the subject form and is correct here because it is the subject of 'is.' 'Whom' is the object form.",
            "difficulty": "Medium"
        },
        {
            "text": "Identify the correct sentence:",
            "options": {
                "A": "The furniture in both rooms are very expensive.",
                "B": "The furniture in both rooms is very expensive.",
                "C": "The furnitures in both rooms are very expensive.",
                "D": "The furnitures in both rooms is very expensive."
            },
            "answer": "B) The furniture in both rooms is very expensive.",
            "explanation": "'Furniture' is an uncountable noun. It does not have a plural form and takes a singular verb.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the grammatically correct option:",
            "options": {
                "A": "He is one of the best players who has ever played for the team.",
                "B": "He is one of the best players who have ever played for the team.",
                "C": "He is one of the best player who has ever played for the team.",
                "D": "He is one of the best players who is ever playing for the team."
            },
            "answer": "B) He is one of the best players who have ever played for the team.",
            "explanation": "The relative pronoun 'who' refers to 'players' (plural), so the verb should be plural: 'have played.'",
            "difficulty": "Hard"
        },
        {
            "text": "Identify the error: 'The report was so lengthy as nobody could finish reading it.'",
            "options": {
                "A": "Replace 'so' with 'such'",
                "B": "Replace 'as' with 'that'",
                "C": "Replace 'could' with 'can'",
                "D": "No error"
            },
            "answer": "B) Replace 'as' with 'that'",
            "explanation": "The correct construction is 'so...that,' not 'so...as.' 'So lengthy that nobody could finish reading it.'",
            "difficulty": "Medium"
        },
        {
            "text": "Which sentence is correct?",
            "options": {
                "A": "Let he and I go to the meeting.",
                "B": "Let him and I go to the meeting.",
                "C": "Let him and me go to the meeting.",
                "D": "Let he and me go to the meeting."
            },
            "answer": "C) Let him and me go to the meeting.",
            "explanation": "'Let' takes the objective case. Both pronouns should be in the objective form: 'him' and 'me.'",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the correct sentence:",
            "options": {
                "A": "She prefers tea than coffee.",
                "B": "She prefers tea over coffee.",
                "C": "She prefers tea to coffee.",
                "D": "She prefers tea from coffee."
            },
            "answer": "C) She prefers tea to coffee.",
            "explanation": "The correct construction is 'prefer X to Y,' not 'prefer X than/over/from Y.'",
            "difficulty": "Easy"
        },
        {
            "text": "Identify the correct sentence:",
            "options": {
                "A": "Scarcely had I reached the office than it started raining.",
                "B": "Scarcely had I reached the office when it started raining.",
                "C": "Scarcely I had reached the office when it started raining.",
                "D": "Scarcely had I reached the office before it started raining."
            },
            "answer": "B) Scarcely had I reached the office when it started raining.",
            "explanation": "'Scarcely...when' is the correct correlative pair, with inversion after 'scarcely.'",
            "difficulty": "Hard"
        },
        {
            "text": "Choose the correct sentence:",
            "options": {
                "A": "The teacher asked the students to set down quietly.",
                "B": "The teacher asked the students to sit down quietly.",
                "C": "The teacher asked the students to sat down quietly.",
                "D": "The teacher asked the students to seated down quietly."
            },
            "answer": "B) The teacher asked the students to sit down quietly.",
            "explanation": "'Sit' means to take a seat (intransitive). 'Set' means to place something (transitive). Students sit; you set objects down.",
            "difficulty": "Easy"
        },
    ]

    for qdata in questions:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    return q


def build_para_jumbles(pdf, start_q):
    """Para Jumbles - 15 questions"""
    q = start_q
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 5: Para Jumbles",
        "Rearrange the given sentences to form a coherent paragraph. "
        "Look for logical connectors, pronoun references, and chronological order."
    )

    questions = [
        {
            "text": "Arrange the following sentences to form a coherent paragraph:\n"
                    "P. However, excessive screen time has been linked to sleep disorders and anxiety.\n"
                    "Q. Digital devices have become an indispensable part of modern life.\n"
                    "R. Experts recommend limiting daily screen time to maintain a healthy balance.\n"
                    "S. They help us communicate, work, and access information instantly.",
            "options": {"A": "Q-S-P-R", "B": "P-Q-S-R", "C": "S-Q-R-P", "D": "Q-P-S-R"},
            "answer": "A) Q-S-P-R",
            "explanation": "Q introduces the topic (digital devices). S elaborates on their benefits. P contrasts with 'However.' R concludes with a recommendation.",
            "difficulty": "Medium"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. This has led to a significant reduction in carbon emissions.\n"
                    "Q. The government introduced a subsidy program for electric vehicles.\n"
                    "R. As a result, sales of electric cars doubled within a year.\n"
                    "S. Many citizens found electric vehicles more affordable.",
            "options": {"A": "Q-S-R-P", "B": "Q-R-S-P", "C": "S-Q-R-P", "D": "P-Q-S-R"},
            "answer": "A) Q-S-R-P",
            "explanation": "Q introduces the cause (subsidy). S shows the immediate effect (affordability). R follows with 'As a result' (doubled sales). P gives the final outcome (reduced emissions).",
            "difficulty": "Medium"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. She was awarded the Nobel Prize for her groundbreaking work.\n"
                    "Q. Marie Curie was born in Warsaw, Poland, in 1867.\n"
                    "R. Despite facing discrimination, she persevered in her scientific pursuits.\n"
                    "S. She moved to Paris to study physics and mathematics.",
            "options": {"A": "Q-S-R-P", "B": "Q-R-S-P", "C": "S-Q-R-P", "D": "P-Q-S-R"},
            "answer": "A) Q-S-R-P",
            "explanation": "The chronological order is: born in Warsaw (Q), moved to Paris (S), faced discrimination but persevered (R), won Nobel Prize (P).",
            "difficulty": "Easy"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. Furthermore, they improve air quality by filtering pollutants.\n"
                    "Q. Trees play a vital role in maintaining ecological balance.\n"
                    "R. Therefore, large-scale afforestation programs are essential.\n"
                    "S. They absorb carbon dioxide and release oxygen through photosynthesis.",
            "options": {"A": "Q-S-P-R", "B": "Q-P-S-R", "C": "S-P-Q-R", "D": "R-Q-S-P"},
            "answer": "A) Q-S-P-R",
            "explanation": "Q introduces the topic. S gives the first benefit. P adds another with 'Furthermore.' R concludes with 'Therefore.'",
            "difficulty": "Easy"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. The findings were published in a leading scientific journal.\n"
                    "Q. A team of researchers conducted a decade-long study on climate change.\n"
                    "R. Their research revealed alarming trends in global temperature rise.\n"
                    "S. This prompted several governments to revise their environmental policies.",
            "options": {"A": "Q-R-P-S", "B": "Q-P-R-S", "C": "R-Q-P-S", "D": "P-Q-R-S"},
            "answer": "A) Q-R-P-S",
            "explanation": "Q introduces the study. R presents the findings. P tells where they were published. S shows the impact of publication.",
            "difficulty": "Medium"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. Initially, the company faced severe financial losses.\n"
                    "Q. A small startup was founded in a garage in 2005.\n"
                    "R. Today, it is valued at over ten billion dollars.\n"
                    "S. However, the founders refused to give up and pivoted their business model.",
            "options": {"A": "Q-P-S-R", "B": "Q-S-P-R", "C": "P-Q-S-R", "D": "Q-R-P-S"},
            "answer": "A) Q-P-S-R",
            "explanation": "Q introduces the startup. P describes early struggles ('Initially'). S shows perseverance ('However'). R reveals the current success ('Today').",
            "difficulty": "Easy"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. Consequently, many students prefer online learning for its convenience.\n"
                    "Q. The internet has revolutionized the field of education.\n"
                    "R. Students can now access courses from top universities around the world.\n"
                    "S. Online platforms offer interactive lessons, quizzes, and certificates.",
            "options": {"A": "Q-R-S-P", "B": "Q-S-R-P", "C": "R-Q-S-P", "D": "S-R-Q-P"},
            "answer": "A) Q-R-S-P",
            "explanation": "Q introduces the topic. R elaborates on access. S adds details about features. P concludes with 'Consequently.'",
            "difficulty": "Medium"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. It was only after years of practice that he mastered the art.\n"
                    "Q. As a child, Ravi showed an unusual interest in painting.\n"
                    "R. His parents enrolled him in an art school at the age of ten.\n"
                    "S. Today, his paintings sell for lakhs at international auctions.",
            "options": {"A": "Q-R-P-S", "B": "Q-P-R-S", "C": "R-Q-P-S", "D": "Q-R-S-P"},
            "answer": "A) Q-R-P-S",
            "explanation": "Q introduces childhood interest. R follows with parents' action. P describes years of practice. S shows the present success.",
            "difficulty": "Easy"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. This discovery could lead to more effective cancer treatments.\n"
                    "Q. Scientists have identified a new protein that inhibits tumor growth.\n"
                    "R. Clinical trials are expected to begin within the next two years.\n"
                    "S. The protein was found to reduce tumor size by sixty percent in laboratory tests.",
            "options": {"A": "Q-S-P-R", "B": "Q-P-S-R", "C": "S-Q-R-P", "D": "Q-R-S-P"},
            "answer": "A) Q-S-P-R",
            "explanation": "Q introduces the discovery. S provides specific data. P explains the potential impact ('This discovery'). R looks to the future.",
            "difficulty": "Medium"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. In contrast, rural areas still struggle with basic internet connectivity.\n"
                    "Q. India's digital infrastructure has grown significantly in recent years.\n"
                    "R. Bridging this digital divide remains a key policy challenge.\n"
                    "S. Major cities now enjoy high-speed broadband and 5G networks.",
            "options": {"A": "Q-S-P-R", "B": "Q-P-S-R", "C": "S-Q-P-R", "D": "Q-S-R-P"},
            "answer": "A) Q-S-P-R",
            "explanation": "Q introduces the general topic. S describes urban progress. P contrasts with 'In contrast' (rural areas). R concludes with the challenge.",
            "difficulty": "Medium"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. The interview panel was impressed by her confidence and knowledge.\n"
                    "Q. She had prepared extensively for months before the interview.\n"
                    "R. Priya applied for a position at a multinational company.\n"
                    "S. She received the offer letter within a week.",
            "options": {"A": "R-Q-P-S", "B": "R-P-Q-S", "C": "Q-R-P-S", "D": "R-Q-S-P"},
            "answer": "A) R-Q-P-S",
            "explanation": "R introduces the event (applying). Q tells about preparation. P describes the interview. S gives the outcome.",
            "difficulty": "Easy"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. Moreover, yoga has been shown to improve mental clarity and focus.\n"
                    "Q. Yoga is an ancient Indian practice that promotes physical and mental well-being.\n"
                    "R. In recent years, it has gained popularity across the globe.\n"
                    "S. Regular practice can reduce stress, improve flexibility, and strengthen the body.",
            "options": {"A": "Q-R-S-P", "B": "Q-S-P-R", "C": "R-Q-S-P", "D": "Q-S-R-P"},
            "answer": "A) Q-R-S-P",
            "explanation": "Q introduces yoga. R notes its recent global popularity. S lists physical benefits. P adds mental benefits with 'Moreover.'",
            "difficulty": "Medium"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. Without bees, many crops would fail, threatening global food supply.\n"
                    "Q. Bees are among the most important pollinators in nature.\n"
                    "R. Scientists are working on strategies to protect bee populations.\n"
                    "S. Unfortunately, bee populations have been declining due to pesticide use and habitat loss.",
            "options": {"A": "Q-P-S-R", "B": "Q-S-P-R", "C": "P-Q-S-R", "D": "Q-S-R-P"},
            "answer": "A) Q-P-S-R",
            "explanation": "Q introduces the topic. P explains their importance. S introduces the problem ('Unfortunately'). R presents the solution.",
            "difficulty": "Medium"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. She completed her doctorate in just three years.\n"
                    "Q. From an early age, Meera displayed exceptional academic talent.\n"
                    "R. Her research on renewable energy has won multiple international awards.\n"
                    "S. She topped her university examinations consistently throughout her undergraduate studies.",
            "options": {"A": "Q-S-P-R", "B": "Q-P-S-R", "C": "S-Q-P-R", "D": "Q-S-R-P"},
            "answer": "A) Q-S-P-R",
            "explanation": "Q introduces early talent. S covers undergraduate success. P describes doctorate completion. R presents recent achievements.",
            "difficulty": "Easy"
        },
        {
            "text": "Arrange the sentences:\n"
                    "P. Nevertheless, the expedition yielded invaluable scientific data.\n"
                    "Q. A team of explorers embarked on a journey to the South Pole.\n"
                    "R. They faced extreme temperatures, blizzards, and equipment failures.\n"
                    "S. The journey took over six months to complete.",
            "options": {"A": "Q-S-R-P", "B": "Q-R-S-P", "C": "S-Q-R-P", "D": "Q-R-P-S"},
            "answer": "A) Q-S-R-P",
            "explanation": "Q introduces the journey. S mentions the duration. R describes the challenges. P concludes with 'Nevertheless' (positive outcome despite difficulties).",
            "difficulty": "Medium"
        },
    ]

    for qdata in questions:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    return q


def build_fill_in_the_blanks(pdf, start_q):
    """Fill in the Blanks - 20 questions"""
    q = start_q
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 6: Fill in the Blanks",
        "Choose the most appropriate word(s) to fill in the blank(s). "
        "These questions test vocabulary, grammar, and contextual understanding."
    )

    pdf.add_subtopic_header("Single Blanks")

    questions_single = [
        {
            "text": "The scientist's theory was so ______ that even experts found it difficult to comprehend.",
            "options": {"A": "abstruse", "B": "lucid", "C": "transparent", "D": "elementary"},
            "answer": "A) abstruse",
            "explanation": "'Abstruse' means difficult to understand. The clue is 'even experts found it difficult to comprehend.'",
            "difficulty": "Hard"
        },
        {
            "text": "The manager's ______ leadership style earned him the respect of his team.",
            "options": {"A": "autocratic", "B": "democratic", "C": "indifferent", "D": "erratic"},
            "answer": "B) democratic",
            "explanation": "A 'democratic' leadership style involves participative decision-making, which typically earns respect.",
            "difficulty": "Easy"
        },
        {
            "text": "Despite his ______ appearance, he was actually very kind and generous.",
            "options": {"A": "amiable", "B": "benign", "C": "stern", "D": "jovial"},
            "answer": "C) stern",
            "explanation": "'Despite' indicates contrast. His appearance (stern/serious) contrasted with his actual nature (kind and generous).",
            "difficulty": "Medium"
        },
        {
            "text": "The company's decision to ______ its overseas operations led to significant cost savings.",
            "options": {"A": "expand", "B": "consolidate", "C": "diversify", "D": "initiate"},
            "answer": "B) consolidate",
            "explanation": "'Consolidate' means to combine or streamline, which leads to cost savings. Expanding or diversifying would typically increase costs.",
            "difficulty": "Medium"
        },
        {
            "text": "The politician's speech was full of ______, offering no concrete plans or solutions.",
            "options": {"A": "substance", "B": "rhetoric", "C": "evidence", "D": "sincerity"},
            "answer": "B) rhetoric",
            "explanation": "'Rhetoric' here refers to language designed to be persuasive but lacking substance. The clue is 'no concrete plans or solutions.'",
            "difficulty": "Medium"
        },
        {
            "text": "The artist's work was a ______ of different styles, blending classical and modern elements.",
            "options": {"A": "contradiction", "B": "rejection", "C": "fusion", "D": "separation"},
            "answer": "C) fusion",
            "explanation": "'Fusion' means a blending or merging of different elements, which matches 'blending classical and modern.'",
            "difficulty": "Easy"
        },
        {
            "text": "His ______ behavior at the party embarrassed his friends and family.",
            "options": {"A": "exemplary", "B": "boorish", "C": "gracious", "D": "modest"},
            "answer": "B) boorish",
            "explanation": "'Boorish' means rough, ill-mannered. It is the only option that would cause embarrassment.",
            "difficulty": "Medium"
        },
        {
            "text": "The new law was ______ to prevent discrimination in the workplace.",
            "options": {"A": "enacted", "B": "repealed", "C": "violated", "D": "ignored"},
            "answer": "A) enacted",
            "explanation": "'Enacted' means passed into law. Laws are enacted (created) to prevent unwanted behavior.",
            "difficulty": "Easy"
        },
        {
            "text": "The witness gave a ______ account of the accident, leaving out several important details.",
            "options": {"A": "comprehensive", "B": "meticulous", "C": "sketchy", "D": "thorough"},
            "answer": "C) sketchy",
            "explanation": "'Sketchy' means lacking detail or completeness. The clue is 'leaving out several important details.'",
            "difficulty": "Easy"
        },
        {
            "text": "The negotiations reached a ______ when neither side was willing to compromise.",
            "options": {"A": "resolution", "B": "breakthrough", "C": "consensus", "D": "deadlock"},
            "answer": "D) deadlock",
            "explanation": "A 'deadlock' is a situation where no progress can be made because neither party will concede.",
            "difficulty": "Easy"
        },
    ]

    for qdata in questions_single:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    pdf.add_subtopic_header("Double Blanks")

    questions_double = [
        {
            "text": "The professor's lectures were so ______ that students often felt ______ and disengaged.",
            "options": {
                "A": "monotonous, bored",
                "B": "engaging, excited",
                "C": "fascinating, inspired",
                "D": "brief, refreshed"
            },
            "answer": "A) monotonous, bored",
            "explanation": "The clue 'disengaged' indicates a negative experience. 'Monotonous' lectures make students 'bored.'",
            "difficulty": "Easy"
        },
        {
            "text": "The ______ of the desert landscape was broken only by the ______ appearance of an oasis.",
            "options": {
                "A": "monotony, occasional",
                "B": "beauty, frequent",
                "C": "chaos, constant",
                "D": "richness, rare"
            },
            "answer": "A) monotony, occasional",
            "explanation": "Deserts are characterized by 'monotony' (sameness), and oases are 'occasional' (rare) features that break this uniformity.",
            "difficulty": "Medium"
        },
        {
            "text": "The CEO's ______ approach to business made the company ______ in the industry.",
            "options": {
                "A": "innovative, a leader",
                "B": "conservative, bankrupt",
                "C": "reckless, successful",
                "D": "timid, dominant"
            },
            "answer": "A) innovative, a leader",
            "explanation": "An 'innovative' approach logically leads to becoming 'a leader' in the industry.",
            "difficulty": "Easy"
        },
        {
            "text": "The author's ______ writing style makes even ______ topics accessible to the general reader.",
            "options": {
                "A": "complex, simple",
                "B": "lucid, complex",
                "C": "obscure, basic",
                "D": "verbose, interesting"
            },
            "answer": "B) lucid, complex",
            "explanation": "'Lucid' (clear) writing can make 'complex' topics accessible. The sentence praises the author's ability to simplify difficult subjects.",
            "difficulty": "Medium"
        },
        {
            "text": "While his ______ in public was impeccable, his ______ life was far from ideal.",
            "options": {
                "A": "behavior, professional",
                "B": "conduct, personal",
                "C": "appearance, social",
                "D": "silence, public"
            },
            "answer": "B) conduct, personal",
            "explanation": "The contrast is between public 'conduct' (impeccable) and 'personal' life (far from ideal).",
            "difficulty": "Medium"
        },
        {
            "text": "The discovery was ______ at first, but its ______ became apparent over time.",
            "options": {
                "A": "ignored, significance",
                "B": "celebrated, failure",
                "C": "obvious, irrelevance",
                "D": "praised, weakness"
            },
            "answer": "A) ignored, significance",
            "explanation": "The contrast ('at first...over time') suggests the discovery was initially 'ignored' but its 'significance' was later recognized.",
            "difficulty": "Medium"
        },
        {
            "text": "The government's ______ measures to control inflation proved to be ______ in the long run.",
            "options": {
                "A": "stringent, effective",
                "B": "lenient, successful",
                "C": "hasty, counterproductive",
                "D": "delayed, immediate"
            },
            "answer": "A) stringent, effective",
            "explanation": "'Stringent' (strict) measures are logically 'effective' in controlling inflation over the long run.",
            "difficulty": "Medium"
        },
        {
            "text": "Her ______ demeanor masked her ______ determination to succeed.",
            "options": {
                "A": "calm, fierce",
                "B": "aggressive, weak",
                "C": "loud, gentle",
                "D": "timid, fading"
            },
            "answer": "A) calm, fierce",
            "explanation": "'Masked' indicates contrast. A 'calm' exterior hid her 'fierce' (intense) determination.",
            "difficulty": "Easy"
        },
        {
            "text": "The ______ of evidence against the accused was so ______ that the jury reached a verdict quickly.",
            "options": {
                "A": "lack, strong",
                "B": "weight, overwhelming",
                "C": "absence, convincing",
                "D": "piece, weak"
            },
            "answer": "B) weight, overwhelming",
            "explanation": "The 'weight' (amount) of evidence was 'overwhelming' (extremely convincing), leading to a quick verdict.",
            "difficulty": "Medium"
        },
        {
            "text": "The ______ between the two countries was resolved through ______ negotiations.",
            "options": {
                "A": "alliance, hostile",
                "B": "dispute, diplomatic",
                "C": "friendship, aggressive",
                "D": "trade, secretive"
            },
            "answer": "B) dispute, diplomatic",
            "explanation": "A 'dispute' (conflict) resolved through 'diplomatic' (peaceful, formal) negotiations is the most logical combination.",
            "difficulty": "Easy"
        },
    ]

    for qdata in questions_double:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    return q


def build_synonyms_antonyms(pdf, start_q):
    """Synonyms & Antonyms - 20 questions"""
    q = start_q
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 7: Synonyms and Antonyms",
        "Choose the word that is closest in meaning (synonym) or most opposite in meaning (antonym) to the given word."
    )

    pdf.add_subtopic_header("Synonyms")

    synonyms = [
        {
            "text": "Choose the synonym of 'ARDUOUS':",
            "options": {"A": "Simple", "B": "Strenuous", "C": "Pleasant", "D": "Brief"},
            "answer": "B) Strenuous",
            "explanation": "'Arduous' means involving a lot of effort and difficulty. 'Strenuous' is the closest synonym.",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the synonym of 'CLANDESTINE':",
            "options": {"A": "Open", "B": "Legal", "C": "Secret", "D": "Famous"},
            "answer": "C) Secret",
            "explanation": "'Clandestine' means kept secret or done secretively, especially because illicit.",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the synonym of 'METICULOUS':",
            "options": {"A": "Careless", "B": "Painstaking", "C": "Hasty", "D": "Casual"},
            "answer": "B) Painstaking",
            "explanation": "'Meticulous' means showing great attention to detail; very careful and precise. 'Painstaking' shares this meaning.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the synonym of 'ELOQUENT':",
            "options": {"A": "Inarticulate", "B": "Persuasive", "C": "Silent", "D": "Confused"},
            "answer": "B) Persuasive",
            "explanation": "'Eloquent' means fluent and persuasive in speaking or writing.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the synonym of 'VINDICATE':",
            "options": {"A": "Accuse", "B": "Condemn", "C": "Justify", "D": "Punish"},
            "answer": "C) Justify",
            "explanation": "'Vindicate' means to clear of blame or suspicion, or to show to be right. 'Justify' is the closest synonym.",
            "difficulty": "Hard"
        },
        {
            "text": "Choose the synonym of 'COPIOUS':",
            "options": {"A": "Scarce", "B": "Abundant", "C": "Tiny", "D": "Expensive"},
            "answer": "B) Abundant",
            "explanation": "'Copious' means abundant in supply or quantity. Both words mean a large amount.",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the synonym of 'INEVITABLE':",
            "options": {"A": "Avoidable", "B": "Unlikely", "C": "Certain", "D": "Optional"},
            "answer": "C) Certain",
            "explanation": "'Inevitable' means certain to happen; unavoidable. 'Certain' conveys the same sense of sureness.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the synonym of 'VORACIOUS':",
            "options": {"A": "Moderate", "B": "Insatiable", "C": "Delicate", "D": "Reluctant"},
            "answer": "B) Insatiable",
            "explanation": "'Voracious' means wanting or devouring great quantities. 'Insatiable' means impossible to satisfy.",
            "difficulty": "Hard"
        },
        {
            "text": "Choose the synonym of 'DILIGENT':",
            "options": {"A": "Lazy", "B": "Industrious", "C": "Negligent", "D": "Indifferent"},
            "answer": "B) Industrious",
            "explanation": "'Diligent' means having or showing care in one's work. 'Industrious' means hard-working.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the synonym of 'AUDACIOUS':",
            "options": {"A": "Timid", "B": "Bold", "C": "Cautious", "D": "Modest"},
            "answer": "B) Bold",
            "explanation": "'Audacious' means showing a willingness to take surprisingly bold risks. 'Bold' is the closest synonym.",
            "difficulty": "Medium"
        },
    ]

    for qdata in synonyms:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    pdf.add_subtopic_header("Antonyms")

    antonyms = [
        {
            "text": "Choose the antonym of 'BENEVOLENT':",
            "options": {"A": "Generous", "B": "Charitable", "C": "Malevolent", "D": "Kind"},
            "answer": "C) Malevolent",
            "explanation": "'Benevolent' means well-meaning and kindly. 'Malevolent' means having or showing a wish to do evil — the exact opposite.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the antonym of 'LOQUACIOUS':",
            "options": {"A": "Talkative", "B": "Verbose", "C": "Taciturn", "D": "Garrulous"},
            "answer": "C) Taciturn",
            "explanation": "'Loquacious' means very talkative. 'Taciturn' means reserved or uncommunicative — the opposite.",
            "difficulty": "Hard"
        },
        {
            "text": "Choose the antonym of 'FRUGAL':",
            "options": {"A": "Thrifty", "B": "Extravagant", "C": "Economical", "D": "Prudent"},
            "answer": "B) Extravagant",
            "explanation": "'Frugal' means sparing or economical. 'Extravagant' means spending freely or excessively.",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the antonym of 'TRANSPARENT':",
            "options": {"A": "Clear", "B": "Obvious", "C": "Opaque", "D": "Visible"},
            "answer": "C) Opaque",
            "explanation": "'Transparent' means allowing light to pass through; clear. 'Opaque' means not able to be seen through; not transparent.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the antonym of 'VAGUE':",
            "options": {"A": "Unclear", "B": "Ambiguous", "C": "Precise", "D": "Hazy"},
            "answer": "C) Precise",
            "explanation": "'Vague' means unclear or not definite. 'Precise' means exact, accurate, and clearly expressed.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the antonym of 'TURBULENT':",
            "options": {"A": "Chaotic", "B": "Stormy", "C": "Tranquil", "D": "Volatile"},
            "answer": "C) Tranquil",
            "explanation": "'Turbulent' means characterized by conflict or disorder. 'Tranquil' means free from disturbance; calm.",
            "difficulty": "Medium"
        },
        {
            "text": "Choose the antonym of 'OBSOLETE':",
            "options": {"A": "Outdated", "B": "Archaic", "C": "Modern", "D": "Ancient"},
            "answer": "C) Modern",
            "explanation": "'Obsolete' means no longer in use; outdated. 'Modern' means current and up-to-date.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the antonym of 'CONCEAL':",
            "options": {"A": "Hide", "B": "Mask", "C": "Bury", "D": "Reveal"},
            "answer": "D) Reveal",
            "explanation": "'Conceal' means to hide or keep secret. 'Reveal' means to make known or show.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the antonym of 'PESSIMISTIC':",
            "options": {"A": "Gloomy", "B": "Optimistic", "C": "Cynical", "D": "Hopeless"},
            "answer": "B) Optimistic",
            "explanation": "'Pessimistic' means tending to see the worst. 'Optimistic' means tending to see the best — direct opposites.",
            "difficulty": "Easy"
        },
        {
            "text": "Choose the antonym of 'PROLIFIC':",
            "options": {"A": "Productive", "B": "Fertile", "C": "Barren", "D": "Creative"},
            "answer": "C) Barren",
            "explanation": "'Prolific' means producing much fruit, foliage, or offspring; highly productive. 'Barren' means unproductive.",
            "difficulty": "Medium"
        },
    ]

    for qdata in antonyms:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    return q


def build_sentence_completion(pdf, start_q):
    """Sentence Completion - 12 questions"""
    q = start_q
    pdf.add_page_break()
    pdf.add_topic_header(
        "Section 8: Sentence Completion",
        "Choose the option that best completes the sentence logically and grammatically. "
        "These questions test your understanding of context, tone, and logical flow."
    )

    questions = [
        {
            "text": "Although the project was completed ahead of schedule, the client was ______ because the quality did not meet expectations.",
            "options": {"A": "elated", "B": "dissatisfied", "C": "indifferent", "D": "grateful"},
            "answer": "B) dissatisfied",
            "explanation": "'Although' signals contrast. Despite the early completion, poor quality made the client 'dissatisfied.'",
            "difficulty": "Easy"
        },
        {
            "text": "The new employee's ______ to adapt to the company culture impressed the management, who had expected a longer adjustment period.",
            "options": {"A": "reluctance", "B": "inability", "C": "eagerness", "D": "refusal"},
            "answer": "C) eagerness",
            "explanation": "Since management was 'impressed' and expected a 'longer adjustment period,' the employee adapted quickly — showing 'eagerness.'",
            "difficulty": "Medium"
        },
        {
            "text": "The evidence presented at the trial was ______, leaving the jury with no doubt about the defendant's guilt.",
            "options": {"A": "circumstantial", "B": "inconclusive", "C": "irrefutable", "D": "fabricated"},
            "answer": "C) irrefutable",
            "explanation": "'No doubt' indicates certainty. 'Irrefutable' means impossible to deny or disprove, fitting the context perfectly.",
            "difficulty": "Medium"
        },
        {
            "text": "The veteran diplomat's ______ handling of the crisis prevented a full-scale military conflict between the two nations.",
            "options": {"A": "clumsy", "B": "inept", "C": "deft", "D": "reckless"},
            "answer": "C) deft",
            "explanation": "'Deft' means demonstrating skill and cleverness. A veteran diplomat's skillful handling prevented conflict.",
            "difficulty": "Medium"
        },
        {
            "text": "The documentary provided a ______ look at the lives of migrant workers, revealing hardships that are often ______.",
            "options": {
                "A": "superficial, highlighted",
                "B": "candid, overlooked",
                "C": "biased, exaggerated",
                "D": "brief, celebrated"
            },
            "answer": "B) candid, overlooked",
            "explanation": "A documentary 'revealing' hardships would provide a 'candid' (honest) look at issues that are typically 'overlooked' (ignored).",
            "difficulty": "Medium"
        },
        {
            "text": "The city's infrastructure was ______ outdated, requiring billions of dollars in ______ to bring it up to modern standards.",
            "options": {
                "A": "slightly, donations",
                "B": "severely, investment",
                "C": "partially, savings",
                "D": "barely, expenses"
            },
            "answer": "B) severely, investment",
            "explanation": "'Billions of dollars' suggests the infrastructure was 'severely' outdated, requiring massive 'investment.'",
            "difficulty": "Easy"
        },
        {
            "text": "Rather than ______ the controversial decision, the spokesperson chose to ______ the media's questions entirely.",
            "options": {
                "A": "defending, evade",
                "B": "supporting, answer",
                "C": "criticizing, ignore",
                "D": "explaining, welcome"
            },
            "answer": "A) defending, evade",
            "explanation": "'Rather than' indicates the spokesperson avoided engagement. Instead of 'defending' the decision, they chose to 'evade' questions.",
            "difficulty": "Medium"
        },
        {
            "text": "The scientist's findings were initially met with ______, but subsequent research ______ her conclusions.",
            "options": {
                "A": "enthusiasm, disproved",
                "B": "skepticism, corroborated",
                "C": "acceptance, contradicted",
                "D": "praise, undermined"
            },
            "answer": "B) skepticism, corroborated",
            "explanation": "'Initially...but' signals contrast. Initial 'skepticism' (doubt) was followed by research that 'corroborated' (confirmed) the findings.",
            "difficulty": "Hard"
        },
        {
            "text": "The novel's protagonist is a ______ character whose moral ambiguity keeps the reader ______ throughout the story.",
            "options": {
                "A": "simple, bored",
                "B": "complex, engaged",
                "C": "predictable, satisfied",
                "D": "flat, entertained"
            },
            "answer": "B) complex, engaged",
            "explanation": "'Moral ambiguity' suggests a 'complex' character, and this complexity keeps readers 'engaged.'",
            "difficulty": "Easy"
        },
        {
            "text": "The company's ______ growth over the past decade can be attributed to its ______ focus on customer satisfaction.",
            "options": {
                "A": "stagnant, wavering",
                "B": "remarkable, unwavering",
                "C": "declining, intense",
                "D": "modest, occasional"
            },
            "answer": "B) remarkable, unwavering",
            "explanation": "'Remarkable' (impressive) growth paired with 'unwavering' (constant, steady) focus creates a logical cause-and-effect relationship.",
            "difficulty": "Easy"
        },
        {
            "text": "The politician's promises sounded ______ during the campaign, but his actions in office proved otherwise, leaving voters feeling ______.",
            "options": {
                "A": "hollow, vindicated",
                "B": "sincere, betrayed",
                "C": "false, satisfied",
                "D": "genuine, delighted"
            },
            "answer": "B) sincere, betrayed",
            "explanation": "The promises 'sounded sincere' but actions 'proved otherwise,' so voters felt 'betrayed.' The contrast is key.",
            "difficulty": "Medium"
        },
        {
            "text": "The museum's latest exhibition is a ______ tribute to the artist's legacy, showcasing works that span her entire ______ career.",
            "options": {
                "A": "fitting, illustrious",
                "B": "poor, mediocre",
                "C": "hasty, brief",
                "D": "controversial, obscure"
            },
            "answer": "A) fitting, illustrious",
            "explanation": "A museum exhibition showcasing an entire career would be a 'fitting' (appropriate) tribute to an 'illustrious' (distinguished) career.",
            "difficulty": "Medium"
        },
    ]

    for qdata in questions:
        pdf.add_question(q, qdata["text"], qdata["options"], qdata["answer"],
                         qdata["explanation"], qdata["difficulty"])
        q += 1

    return q


def build_table_of_contents(pdf):
    """Add a Table of Contents page"""
    pdf.add_topic_header("Table of Contents")
    toc_data = [
        ["Section", "Topic", "Questions"],
        ["1", "Reading Comprehension", "Q1 - Q25 (25 questions)"],
        ["2", "Grammar", "Q26 - Q45 (20 questions)"],
        ["3", "Vocabulary", "Q46 - Q65 (20 questions)"],
        ["4", "Sentence Correction", "Q66 - Q85 (20 questions)"],
        ["5", "Para Jumbles", "Q86 - Q100 (15 questions)"],
        ["6", "Fill in the Blanks", "Q101 - Q120 (20 questions)"],
        ["7", "Synonyms and Antonyms", "Q121 - Q140 (20 questions)"],
        ["8", "Sentence Completion", "Q141 - Q152 (12 questions)"],
    ]
    pdf.add_table(toc_data, col_widths=[60, 220, 180])
    pdf.add_text("")
    pdf.add_text("<b>Total: 152 Questions</b>", style="Normal")
    pdf.add_text("")
    pdf.add_tip(
        "For TCS NQT, focus on reading speed and accuracy. Practice identifying keywords "
        "in questions before reading the full passage. In grammar questions, eliminate options "
        "with obvious errors first. For vocabulary, build a habit of learning 10 new words daily."
    )
    pdf.add_tip(
        "Time management is crucial. Allocate roughly 30-35 minutes to the Verbal Ability section. "
        "Do not spend more than 1 minute on any single question. Mark and return to difficult questions."
    )
    pdf.add_page_break()


def main():
    output_path = os.path.join(
        os.path.dirname(__file__), '..', '01-Aptitude', 'PDFs', 'Verbal-Ability.pdf'
    )
    output_path = os.path.abspath(output_path)

    pdf = TCSNQTPDFGenerator(
        output_path=output_path,
        title="Verbal Ability",
        subject="TCS NQT Preparation - Complete Question Bank"
    )

    # Cover page
    pdf.add_cover_page()

    # Table of Contents
    build_table_of_contents(pdf)

    # Build all sections
    q = 1
    q = build_reading_comprehension(pdf, q)   # 25 questions
    q = build_grammar(pdf, q)                  # 20 questions
    q = build_vocabulary(pdf, q)               # 20 questions
    q = build_sentence_correction(pdf, q)      # 20 questions
    q = build_para_jumbles(pdf, q)             # 15 questions
    q = build_fill_in_the_blanks(pdf, q)       # 20 questions
    q = build_synonyms_antonyms(pdf, q)        # 20 questions
    q = build_sentence_completion(pdf, q)      # 12 questions

    total = q - 1
    print(f"Total questions added: {total}")

    # Generate PDF
    pdf.generate()
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()
