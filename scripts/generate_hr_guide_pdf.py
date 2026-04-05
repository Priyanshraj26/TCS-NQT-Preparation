#!/usr/bin/env python3
"""
Generate HR Interview Guide PDF for TCS NQT Preparation
Comprehensive guide with 50+ HR questions, STAR method behavioral answers,
technical discussion prep, and TCS-specific preparation material.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.pdf_generator import TCSNQTPDFGenerator


def build_pdf():
    output_path = os.path.join(os.path.dirname(__file__), '..', '05-HR-Interview', 'HR-Interview-Guide.pdf')
    pdf = TCSNQTPDFGenerator(
        output_path=output_path,
        title="HR Interview Guide",
        subject="TCS NQT - Complete HR Interview Preparation"
    )

    pdf.add_cover_page()

    # =========================================================================
    # TABLE OF CONTENTS
    # =========================================================================
    pdf.add_topic_header("Table of Contents")
    pdf.add_text("Part 1: Common HR Questions (50+ Questions with Model Answers) .............. Page 3")
    pdf.add_text("Part 2: Behavioral Questions (30+ STAR Method Answers) ............................ Page 18")
    pdf.add_text("Part 3: Technical Discussion Preparation .................................................... Page 30")
    pdf.add_text("Part 4: Questions to Ask the Interviewer .................................................... Page 34")
    pdf.add_text("Part 5: Do's and Don'ts ........................................................................... Page 37")
    pdf.add_text("Part 6: TCS-Specific Preparation .............................................................. Page 42")
    pdf.add_page_break()

    # =========================================================================
    # PART 1: COMMON HR QUESTIONS
    # =========================================================================
    pdf.add_topic_header("Part 1: Common HR Questions",
                         "This section covers the most frequently asked HR questions in TCS interviews. "
                         "Each question comes with a model answer framework you can personalize. "
                         "Remember: never memorize answers word-for-word. Understand the intent behind "
                         "each question and craft authentic responses.")

    q = 1

    # --- Self Introduction ---
    pdf.add_subtopic_header("1.1 Self-Introduction & Personal Questions")

    pdf.add_question(q, "Tell me about yourself.",
        answer="Use the Present-Past-Future formula.",
        explanation=(
            "Template: 'Good morning/afternoon. My name is [Name]. I recently completed my [Degree] "
            "from [College] with a CGPA of [X]. During my academic journey, I developed a strong interest "
            "in [relevant field]. I worked on projects like [Project 1] and [Project 2], which gave me "
            "hands-on experience in [skills]. I also have skills in [programming languages/tools]. "
            "Outside academics, I enjoy [hobby/activity] which has helped me develop [soft skill]. "
            "I am now looking forward to starting my professional career at a reputed organization like TCS "
            "where I can apply my skills and continue to grow.' Keep it under 2 minutes. Practice until it "
            "sounds natural, not rehearsed."
        ))
    q += 1

    pdf.add_question(q, "Walk me through your resume.",
        answer="Highlight academics, skills, projects, and achievements chronologically.",
        explanation=(
            "Start with education, mention key technical skills, walk through 1-2 important projects "
            "briefly, mention any internships or certifications, and end with your career objective. "
            "Do not simply read your resume aloud. Instead, connect the dots and show progression. "
            "Example: 'As you can see from my resume, I pursued B.Tech in CSE from XYZ University. "
            "I focused heavily on programming and data structures, which led me to build a project on [X]. "
            "This experience strengthened my problem-solving abilities and made me confident about working "
            "in the IT industry.'"
        ))
    q += 1

    pdf.add_question(q, "What are your hobbies and interests?",
        answer="Choose hobbies that demonstrate positive traits relevant to work.",
        explanation=(
            "Good examples: Reading (shows continuous learning), playing chess (strategic thinking), "
            "blogging (communication skills), team sports (teamwork), coding challenges (passion for "
            "technology). Avoid generic answers like 'listening to music' or 'watching movies' unless you "
            "can connect them to a skill. Example: 'I enjoy solving problems on competitive programming "
            "platforms like HackerRank. It has helped me improve my logical thinking and ability to work "
            "under time pressure. I also enjoy playing badminton, which has taught me the value of quick "
            "decision-making and staying physically active.'"
        ))
    q += 1

    pdf.add_question(q, "Describe yourself in one word.",
        answer="Choose a word that reflects your strongest professional quality.",
        explanation=(
            "Good choices: Adaptable, Determined, Curious, Dependable, Resilient, or Versatile. "
            "Always be ready to justify your choice with an example. Example: 'I would describe myself "
            "as Adaptable. During my final year, our project requirements changed midway, and I quickly "
            "learned a new framework within two weeks to deliver the project on time. This ability to "
            "adapt to changing situations is something I take pride in.'"
        ))
    q += 1

    pdf.add_question(q, "What is your greatest achievement so far?",
        answer="Pick an achievement that shows initiative, effort, and results.",
        explanation=(
            "Choose something meaningful: academic award, project completion, competition win, or "
            "overcoming a personal challenge. Use the CAR format (Challenge, Action, Result). "
            "Example: 'My greatest achievement was leading a team of four to develop a hospital management "
            "system that won the best project award in our department. The challenge was integrating "
            "multiple modules with real-time data synchronization. I coordinated the team, divided tasks "
            "based on individual strengths, and we delivered it two days before the deadline.'"
        ))
    q += 1

    # --- Why TCS ---
    pdf.add_subtopic_header("1.2 Company & Career Questions")

    pdf.add_question(q, "Why do you want to join TCS?",
        answer="Show genuine knowledge of TCS and align it with your career goals.",
        explanation=(
            "Key points to mention: TCS is the largest IT services company in India and a global leader. "
            "TCS has a strong learning culture with programs like the Initial Learning Program (ILP). "
            "TCS offers diverse project exposure across domains (banking, healthcare, retail, etc.). "
            "TCS values innovation (TCS Pace, TCS Research). TCS has a stable work environment with "
            "excellent employee development programs. Example: 'TCS has always been my top choice because "
            "of its reputation as a global IT leader and its commitment to employee growth. The Initial "
            "Learning Program is something that excites me as a fresher, because it provides structured "
            "training to build a strong foundation. I also admire how TCS invests in innovation through "
            "initiatives like TCS Pace and its research labs.'"
        ))
    q += 1

    pdf.add_question(q, "Why should we hire you?",
        answer="Connect your skills and qualities to what TCS needs in a fresher.",
        explanation=(
            "Focus on: your technical foundation, willingness to learn, adaptability, and team spirit. "
            "Example: 'You should hire me because I bring a solid technical foundation in programming and "
            "problem-solving, combined with a genuine eagerness to learn and grow. My project experience "
            "has taught me to work effectively in teams and meet deadlines. I am adaptable, which means "
            "I can quickly pick up new technologies as required. Most importantly, I am committed to "
            "contributing my best to whatever team I join and growing alongside the organization.'"
        ))
    q += 1

    pdf.add_question(q, "Where do you see yourself in 5 years?",
        answer="Show ambition aligned with realistic growth within TCS.",
        explanation=(
            "Avoid saying you want to start your own company or do an MBA. Show loyalty and growth intent. "
            "Example: 'In five years, I see myself as a technically proficient professional who has grown "
            "into a role with greater responsibilities, possibly leading a small team. I want to develop "
            "deep expertise in a technology domain while also building my project management and leadership "
            "skills. I believe TCS provides the right platform for this kind of holistic growth, and I "
            "want to be someone the organization can rely on for delivering quality work.'"
        ))
    q += 1

    pdf.add_question(q, "What are your salary expectations?",
        answer="Be diplomatic and show that learning matters more than compensation.",
        explanation=(
            "As a fresher, you typically get the package mentioned in the offer (3.36 LPA for Ninja, "
            "7 LPA for Digital, 11.5 LPA for Prime). Example: 'As a fresher, my primary expectation is "
            "to gain quality experience and learn from industry experts. I am confident that TCS offers "
            "a fair and competitive compensation package for freshers, and I am comfortable with the "
            "standard package offered. What matters more to me at this stage is the opportunity to learn "
            "and build a strong career foundation.' Never negotiate aggressively in an HR interview."
        ))
    q += 1

    pdf.add_question(q, "Are you willing to relocate anywhere in India?",
        answer="Always say yes enthusiastically.",
        explanation=(
            "TCS operates across India and may assign you to any location based on project needs. "
            "Saying no or showing hesitation is a red flag. Example: 'Absolutely, I am completely willing "
            "to relocate anywhere in India. I see it as an opportunity to experience different cultures "
            "and broaden my perspective. I understand that project requirements may demand relocation, "
            "and I am fully prepared for that. In fact, I look forward to the experience of living and "
            "working in a new city.'"
        ))
    q += 1

    pdf.add_question(q, "Are you willing to work in shifts or night shifts?",
        answer="Yes, express willingness and understanding of client requirements.",
        explanation=(
            "TCS serves global clients across time zones. Shift work is common. Example: 'Yes, I am "
            "willing to work in any shift. I understand that TCS has clients across the globe, and "
            "serving them effectively sometimes requires working in different time zones. I am flexible "
            "and can adapt my schedule accordingly. I believe this is part of working in a global IT "
            "company, and I am prepared for it.'"
        ))
    q += 1

    pdf.add_question(q, "Do you have any backlogs or gaps in education?",
        answer="Be honest and positive about what you learned from the experience.",
        explanation=(
            "If you have backlogs: 'Yes, I had [X] backlogs during my [year], which I have since cleared. "
            "That phase taught me the importance of consistency and proper time management. I took it as a "
            "learning experience and improved my study approach significantly, which is reflected in my "
            "later semester results.' If you have a gap year: 'I took a gap year to prepare for competitive "
            "exams / due to health reasons / family circumstances. During this time, I also utilized the "
            "opportunity to learn [skill/certification]. It was a period of personal growth that made me "
            "more focused and determined.' Never lie about gaps or backlogs."
        ))
    q += 1

    pdf.add_question(q, "Why is your CGPA low?",
        answer="Own it honestly and show growth or compensating strengths.",
        explanation=(
            "Example: 'I acknowledge that my CGPA does not fully reflect my capabilities. During my early "
            "semesters, I was still figuring out how to balance academics with my interest in practical "
            "programming and projects. As you can see, my later semester grades improved significantly "
            "because I developed better study habits. I have also invested heavily in building practical "
            "skills through projects and certifications, which I believe are equally important in the "
            "IT industry. My CGPA taught me a valuable lesson about consistency, and I have applied that "
            "lesson to everything I do now.' Always show upward trend if possible."
        ))
    q += 1

    pdf.add_question(q, "Why did you choose your branch/stream of engineering?",
        answer="Show genuine interest and connect it to your career path.",
        explanation=(
            "For CS/IT: 'I chose Computer Science because I was fascinated by how technology can solve "
            "real-world problems. From the moment I wrote my first program in school, I knew this was "
            "the field for me. My coursework in data structures, algorithms, and software engineering "
            "has reinforced my passion for building efficient solutions.' "
            "For non-CS branches: 'I chose [branch] because of my interest in [relevant area]. "
            "However, during my studies, I discovered a strong passion for programming and software "
            "development. I invested time in learning programming languages and building projects, "
            "which prepared me well for the IT industry. My [branch] background gives me a unique "
            "perspective in understanding domain-specific problems.'"
        ))
    q += 1

    pdf.add_question(q, "Why not go for higher studies (M.Tech/MBA)?",
        answer="Show preference for practical learning and industry experience.",
        explanation=(
            "Example: 'I believe that at this stage of my career, gaining practical industry experience "
            "will accelerate my growth more than additional academic degrees. I want to apply the "
            "theoretical knowledge I have gained and learn from real-world projects. Companies like TCS "
            "also offer opportunities for continuous learning through internal certifications and training "
            "programs. I may consider higher studies in the future if I feel it would add value to my "
            "career path, but right now, I am eager to start working and building practical expertise.'"
        ))
    q += 1

    # --- Strengths and Weaknesses ---
    pdf.add_subtopic_header("1.3 Strengths, Weaknesses & Self-Awareness")

    pdf.add_question(q, "What are your strengths?",
        answer="Pick 2-3 strengths with concrete examples.",
        explanation=(
            "Good strengths for TCS: Quick learner, team player, problem-solving ability, adaptability, "
            "attention to detail, good communication. Example: 'My key strengths are my ability to learn "
            "quickly and my problem-solving mindset. For instance, during my final year project, I had to "
            "learn React.js from scratch within two weeks to meet the project timeline, and I was able to "
            "build a functional frontend. Another strength is my ability to work well in teams. I actively "
            "listen to others ideas and believe that collaboration leads to better outcomes.'"
        ))
    q += 1

    pdf.add_question(q, "What are your weaknesses?",
        answer="Share a genuine weakness and show how you are working to improve it.",
        explanation=(
            "Avoid cliches like 'I am a perfectionist' or 'I work too hard.' Choose a real but non-critical "
            "weakness. Example: 'One area I am working on is public speaking. While I am comfortable in "
            "small group discussions, I tend to get nervous when presenting to large audiences. To address "
            "this, I have been participating in college seminars and presentation events. I have seen "
            "noticeable improvement in the last year, and I am committed to continuing to develop this "
            "skill.' Other good options: overthinking decisions (working on being more decisive), "
            "being too detail-oriented (learning to balance detail with speed), or difficulty saying no "
            "(learning to prioritize better)."
        ))
    q += 1

    pdf.add_question(q, "How do you handle stress and pressure?",
        answer="Show practical coping strategies and give an example.",
        explanation=(
            "Example: 'I handle pressure by breaking down large tasks into smaller, manageable steps and "
            "prioritizing them. During my final semester, I had to manage my project submission, exam "
            "preparation, and placement preparation simultaneously. I created a detailed weekly schedule, "
            "allocated specific time blocks for each activity, and made sure to take short breaks to "
            "stay fresh. This structured approach helped me perform well in all three areas. I also "
            "believe that some amount of pressure actually helps me stay focused and deliver better work.'"
        ))
    q += 1

    pdf.add_question(q, "How do you handle criticism?",
        answer="Show maturity and a growth mindset.",
        explanation=(
            "Example: 'I view constructive criticism as an opportunity to improve. In my project team, "
            "my team lead once pointed out that my code lacked proper comments and documentation. Initially, "
            "I felt a bit defensive, but I realized they were right. I started following coding best "
            "practices and even created a documentation template for our team. Looking back, that feedback "
            "significantly improved my coding habits. I believe feedback is essential for growth, and I "
            "actively seek it to identify my blind spots.'"
        ))
    q += 1

    pdf.add_question(q, "What motivates you?",
        answer="Connect your motivation to professional growth and making an impact.",
        explanation=(
            "Example: 'I am motivated by the opportunity to solve meaningful problems and see the tangible "
            "impact of my work. When I built my college project, seeing students actually use the "
            "application I created gave me immense satisfaction. I am also driven by continuous learning - "
            "the IT industry is constantly evolving, and the chance to learn new technologies and "
            "methodologies keeps me excited. Working alongside talented people and being part of a team "
            "that delivers quality work also motivates me greatly.'"
        ))
    q += 1

    # --- Project Questions ---
    pdf.add_subtopic_header("1.4 Project & Technical Background")

    pdf.add_question(q, "Tell me about your projects.",
        answer="Use the structure: Problem - Technology - Your Role - Outcome.",
        explanation=(
            "Template: 'My main project was [Project Name], which aimed to solve [Problem]. We used "
            "[Technologies] to build the solution. My specific contributions included [your tasks]. "
            "The outcome was [result/learning]. For example: My final year project was a Smart Attendance "
            "System using Face Recognition. The problem was that manual attendance was time-consuming "
            "and prone to proxy attendance. I used Python, OpenCV, and a MySQL database. My role was "
            "developing the face detection module and integrating it with the database. The system "
            "achieved 95% accuracy and reduced attendance time by 70%. This project taught me the "
            "importance of testing and iterative development.' Be ready for follow-up technical questions."
        ))
    q += 1

    pdf.add_question(q, "What challenges did you face in your project?",
        answer="Describe a specific challenge and how you overcame it.",
        explanation=(
            "Example: 'The biggest challenge was handling low-light conditions in face recognition, which "
            "significantly reduced accuracy. I researched various image preprocessing techniques and "
            "implemented histogram equalization and adaptive thresholding to enhance image quality before "
            "feeding it to the recognition model. After multiple iterations of testing and parameter "
            "tuning, we improved the accuracy from 78% to 95% in normal lighting and 88% in low-light "
            "conditions. This taught me the importance of iterative problem-solving and not giving up "
            "when the first approach does not work.'"
        ))
    q += 1

    pdf.add_question(q, "What technologies/programming languages do you know?",
        answer="Be honest and categorize your skill levels.",
        explanation=(
            "Example: 'I am most proficient in Python and Java, which I have used extensively in my "
            "projects and coursework. I have a good working knowledge of C and SQL. On the web development "
            "side, I have experience with HTML, CSS, JavaScript, and React.js. For databases, I have "
            "worked with MySQL and MongoDB. I also have basic familiarity with Git for version control "
            "and have used AWS for deploying a small application. I am always eager to learn new "
            "technologies as required.' Only mention technologies you can answer questions about."
        ))
    q += 1

    pdf.add_question(q, "What do you know about TCS?",
        answer="Demonstrate thorough research about TCS.",
        explanation=(
            "Key facts: TCS (Tata Consultancy Services) was founded in 1968 and is headquartered in "
            "Mumbai. It is part of the Tata Group and is India's largest IT services company. TCS has "
            "over 600,000 employees across 55+ countries. The current CEO is K Krithivasan. TCS reported "
            "revenue of over $29 billion. TCS was the first Indian IT company to reach $100 billion market "
            "cap. Key services include IT services, consulting, and digital solutions. TCS serves clients "
            "in banking, insurance, telecom, retail, and manufacturing. TCS invests heavily in innovation "
            "through TCS Research and TCS Pace. The company motto focuses on 'Building on Belief.' "
            "Mention specific things that impress you about TCS."
        ))
    q += 1

    # --- Teamwork & Leadership ---
    pdf.add_subtopic_header("1.5 Teamwork & Interpersonal Skills")

    pdf.add_question(q, "Are you a team player or do you prefer working alone?",
        answer="Show flexibility but lean toward teamwork.",
        explanation=(
            "Example: 'I enjoy working in both settings, but I particularly value teamwork because "
            "collaboration often leads to better solutions. In my project team, we had members with "
            "different strengths - one was great at frontend design, another at backend logic, and I "
            "focused on database integration. Together, we built something better than any of us could "
            "have individually. That said, I am equally comfortable working independently when a task "
            "requires focused individual effort, such as debugging or research. I believe the best "
            "professionals can adapt to both modes of working.'"
        ))
    q += 1

    pdf.add_question(q, "How do you handle disagreements with team members?",
        answer="Show maturity, respect for others, and focus on solutions.",
        explanation=(
            "Example: 'When I disagree with a team member, I first try to understand their perspective "
            "by listening carefully. I believe most disagreements arise from different viewpoints, not "
            "bad intentions. I share my perspective with facts and reasoning rather than emotions. "
            "If we still cannot agree, I suggest we test both approaches or seek input from a third "
            "person. In one of my projects, my teammate and I disagreed on the database design. Instead "
            "of arguing, we created small prototypes of both approaches and compared performance. "
            "His approach turned out to be more efficient for our use case, and I was happy to learn "
            "from that experience.'"
        ))
    q += 1

    pdf.add_question(q, "Describe a time you worked in a team.",
        answer="Give a specific example with your role and the outcome.",
        explanation=(
            "Example: 'During my sixth semester, I was part of a four-member team for our mini project. "
            "We built an e-commerce website. I took responsibility for the backend APIs and database "
            "design, while others handled the frontend and payment integration. We used daily 15-minute "
            "stand-up meetings to track progress and resolve blockers. When one team member fell sick "
            "for a week, I helped cover their tasks alongside mine to keep us on schedule. We delivered "
            "the project on time and received an A grade. This experience taught me that communication "
            "and mutual support are the foundations of good teamwork.'"
        ))
    q += 1

    pdf.add_question(q, "Have you ever led a team? Tell me about it.",
        answer="Describe your leadership style and a concrete outcome.",
        explanation=(
            "Example: 'I led a team of five for our college technical fest event. I was responsible for "
            "planning the coding competition, coordinating with the college administration, and managing "
            "participant registrations. I delegated tasks based on each members strengths, set clear "
            "deadlines, and maintained a shared tracker for progress. We faced a budget constraint, so I "
            "reached out to local tech companies for sponsorship and secured funding for prizes. The event "
            "had 120 participants, which was the highest in our college fest. I learned that effective "
            "leadership is about empowering others and removing obstacles for them.'"
        ))
    q += 1

    # --- Situational ---
    pdf.add_subtopic_header("1.6 Situational & Hypothetical Questions")

    pdf.add_question(q, "What would you do if you are assigned a technology you do not know?",
        answer="Show eagerness to learn and a practical approach.",
        explanation=(
            "Example: 'I would be excited about the opportunity to learn something new. My approach would "
            "be: First, I would go through the official documentation and online tutorials to build a "
            "foundational understanding. Then, I would practice by building small projects or solving "
            "exercises. I would also reach out to colleagues who are experienced in that technology "
            "for guidance and best practices. I have done this before when I had to learn React.js for "
            "my project - within two weeks, I was able to build functional components. I believe the "
            "ability to learn new technologies quickly is one of the most important skills in IT.'"
        ))
    q += 1

    pdf.add_question(q, "What would you do if your manager asks you to do something you disagree with?",
        answer="Show professionalism while maintaining your ability to voice concerns.",
        explanation=(
            "Example: 'I would first try to understand the reasoning behind the decision by asking "
            "clarifying questions respectfully. There might be context or constraints I am not aware of. "
            "If I still have concerns, I would share them professionally, presenting data or examples to "
            "support my viewpoint. However, if after discussion the manager still wants to proceed their "
            "way, I would respect the decision and execute it to the best of my ability. I believe in "
            "trusting the experience of senior colleagues while also contributing my perspective "
            "constructively. At the end of the day, the team's success matters more than individual "
            "opinions.'"
        ))
    q += 1

    pdf.add_question(q, "If you get a better offer from another company, will you leave TCS?",
        answer="Show loyalty and long-term thinking without being unrealistic.",
        explanation=(
            "Example: 'I am not someone who chases offers. I believe in committing to an organization "
            "and growing with it. If I join TCS, my focus will be on learning, contributing, and building "
            "a meaningful career here. TCS offers tremendous opportunities for growth across technologies "
            "and domains, and I plan to explore those opportunities fully. I believe that job satisfaction "
            "comes from doing meaningful work, continuous learning, and working with good people, and "
            "TCS provides all of these. So I do not see myself looking elsewhere.'"
        ))
    q += 1

    pdf.add_question(q, "What would you do if you are not placed in your preferred role/technology?",
        answer="Show flexibility and a positive attitude.",
        explanation=(
            "Example: 'I would approach it with an open mind. Every technology and domain has its own "
            "depth and interesting challenges. Many successful professionals have found their passion in "
            "areas they did not initially choose. I would give my best to learn and excel in whatever "
            "role I am assigned, and I am confident I would find it engaging once I dive deep into it. "
            "I believe adaptability is a key trait for success in the IT industry, and this would be an "
            "opportunity to demonstrate that quality.'"
        ))
    q += 1

    # --- More Common Questions ---
    pdf.add_subtopic_header("1.7 Additional Common Questions")

    pdf.add_question(q, "Tell me something about yourself that is not on your resume.",
        answer="Share a personal quality or experience that adds depth to your profile.",
        explanation=(
            "Example: 'Something that is not on my resume is that I volunteer at a local NGO every "
            "weekend, teaching basic computer skills to underprivileged children. I have been doing this "
            "for the past two years, and it has been one of the most fulfilling experiences of my life. "
            "It has improved my patience, communication skills, and ability to explain complex concepts "
            "in simple terms. It also reinforced my belief that technology can be a great equalizer, "
            "which is one reason I am passionate about the IT industry.'"
        ))
    q += 1

    pdf.add_question(q, "How do you prioritize your tasks when you have multiple deadlines?",
        answer="Show a structured approach to time management.",
        explanation=(
            "Example: 'I use a combination of urgency and importance to prioritize tasks. First, I list "
            "all tasks with their deadlines. Then I categorize them: urgent and important tasks come "
            "first, followed by important but not urgent tasks. I also estimate the time required for "
            "each task and create a realistic schedule. I use tools like to-do lists or simple "
            "spreadsheets to track progress. During my final semester, I managed project work, exam "
            "preparation, and placement preparation simultaneously using this approach, and I was able "
            "to perform well in all three areas.'"
        ))
    q += 1

    pdf.add_question(q, "What is your biggest regret so far?",
        answer="Choose something that led to positive change.",
        explanation=(
            "Example: 'My biggest regret is not starting competitive programming earlier in my college "
            "life. I only began in my third year and realized how much it improves problem-solving and "
            "coding speed. If I had started in my first year, I would have been much more proficient "
            "by now. However, this regret has taught me the value of starting early and not "
            "procrastinating. I now apply this lesson to everything - if something seems valuable, "
            "I start working on it immediately rather than waiting for the right time.'"
        ))
    q += 1

    pdf.add_question(q, "Do you have any questions for us?",
        answer="Always have 2-3 thoughtful questions prepared (covered in Part 4).",
        explanation=(
            "Saying 'No, I don't have any questions' suggests lack of interest. Prepare questions about "
            "the role, team, learning opportunities, or TCS initiatives. Examples: 'Can you tell me more "
            "about the Initial Learning Program?', 'What kind of projects are freshers typically assigned "
            "to?', 'How does TCS support continuous learning for employees?' See Part 4 for a complete list."
        ))
    q += 1

    pdf.add_question(q, "How would your friends describe you?",
        answer="Align the description with professional qualities.",
        explanation=(
            "Example: 'My friends would describe me as someone who is reliable and always ready to help. "
            "I am usually the person they come to when they need help understanding a difficult concept "
            "or solving a coding problem. They would also say I am organized - I am often the one "
            "creating study plans or coordinating group projects. I think they appreciate that I am "
            "a good listener who gives practical advice rather than just sympathizing.'"
        ))
    q += 1

    pdf.add_question(q, "What makes you unique?",
        answer="Highlight a combination of qualities that sets you apart.",
        explanation=(
            "Example: 'What makes me unique is my combination of technical skills and strong communication "
            "abilities. Many engineers are technically strong but struggle to communicate their ideas "
            "clearly, or they are great communicators but lack technical depth. I have actively worked on "
            "both aspects - through my projects and coursework for technical skills, and through "
            "presentations, blogging, and team collaborations for communication. I believe this "
            "combination will help me bridge the gap between technical and non-technical stakeholders.'"
        ))
    q += 1

    pdf.add_question(q, "What do you do in your free time?",
        answer="Show productive use of time that demonstrates positive traits.",
        explanation=(
            "Example: 'In my free time, I enjoy exploring new technologies through online courses and "
            "tutorials. I recently completed a course on cloud computing basics. I also spend time "
            "reading technical blogs and articles to stay updated with industry trends. On weekends, "
            "I play cricket with my friends, which helps me unwind and also keeps me physically active. "
            "I find that this balance between intellectual and physical activities helps me stay fresh "
            "and productive.'"
        ))
    q += 1

    pdf.add_question(q, "Have you done any internships?",
        answer="If yes, describe it well. If no, show equivalent experience.",
        explanation=(
            "With internship: 'Yes, I interned at [Company] for [duration], where I worked on [project/"
            "task]. I learned about [skills/technologies] and contributed to [achievement]. The experience "
            "gave me a taste of professional work culture and reinforced my desire to work in the IT "
            "industry.' Without internship: 'While I did not have a formal internship, I gained "
            "practical experience through my academic projects and self-directed learning. My final year "
            "project was essentially a full-stack application that I built from scratch, which gave me "
            "exposure to the full software development lifecycle. I also completed several online "
            "certifications to supplement my learning.'"
        ))
    q += 1

    pdf.add_question(q, "What is your opinion about the IT industry in India?",
        answer="Show awareness and optimism about the industry.",
        explanation=(
            "Example: 'The Indian IT industry is at an exciting juncture. It has evolved from being "
            "primarily an outsourcing destination to now leading innovation in areas like AI, cloud "
            "computing, and digital transformation. Companies like TCS are at the forefront of this "
            "evolution, helping global clients navigate their digital journeys. With initiatives like "
            "Digital India and the growing startup ecosystem, I believe India will continue to be a "
            "major global technology hub. As a fresher, I find it exciting to enter the industry at "
            "a time when there are so many opportunities for innovation and impact.'"
        ))
    q += 1

    pdf.add_question(q, "What is the difference between hard work and smart work?",
        answer="Show understanding that both are important and complementary.",
        explanation=(
            "Example: 'Hard work is about putting in consistent effort and dedication, while smart work "
            "is about finding efficient ways to achieve the same goal with optimized effort. I believe "
            "the best results come from combining both. For example, in my project, hard work meant "
            "spending hours debugging and testing code. Smart work meant using debugging tools, writing "
            "unit tests, and following coding best practices to reduce bugs in the first place. Neither "
            "can replace the other - you need the discipline of hard work and the intelligence of smart "
            "work to truly excel.'"
        ))
    q += 1

    pdf.add_question(q, "Are you comfortable with a bond/service agreement?",
        answer="Show understanding and acceptance of the commitment.",
        explanation=(
            "Example: 'Yes, I am completely comfortable with a service agreement. I understand that TCS "
            "invests significantly in training and developing freshers through the ILP, and a service "
            "agreement is a reasonable expectation in return. Moreover, I am joining TCS with the "
            "intention of building a long-term career here, so the service period aligns perfectly with "
            "my plans. I see it as a mutual commitment - TCS commits to developing me, and I commit to "
            "contributing my skills to TCS.'"
        ))
    q += 1

    pdf.add_question(q, "What is your definition of success?",
        answer="Show a balanced and mature perspective.",
        explanation=(
            "Example: 'To me, success is a journey, not a destination. It means continuously growing, "
            "learning from experiences, and making a positive impact in whatever I do. Professionally, "
            "success means becoming someone my team can depend on, solving meaningful problems, and "
            "growing into roles with greater responsibility. Personally, it means maintaining a healthy "
            "work-life balance and being someone my family and friends are proud of. I do not measure "
            "success only by job titles or salary - it is about the quality of work I do and the "
            "relationships I build along the way.'"
        ))
    q += 1

    pdf.add_question(q, "Who is your role model and why?",
        answer="Choose someone whose qualities relate to professional success.",
        explanation=(
            "Example: 'My role model is Ratan Tata. What inspires me most is his combination of humility "
            "and visionary leadership. He led the Tata Group to become a global conglomerate while "
            "maintaining the highest ethical standards. His emphasis on giving back to society through "
            "the Tata Trusts resonates with my belief that success should be used to create positive "
            "impact. Most importantly, his ability to stay grounded despite immense success teaches me "
            "that character matters more than accomplishments.' Note: Choosing someone from the Tata "
            "Group is a nice touch for a TCS interview, but only if your admiration is genuine."
        ))
    q += 1

    pdf.add_question(q, "How do you stay updated with technology trends?",
        answer="Show proactive learning habits.",
        explanation=(
            "Example: 'I follow several technology blogs and websites like TechCrunch, Medium, and "
            "GeeksforGeeks. I subscribe to newsletters from companies like Google and Microsoft for "
            "updates on new technologies. I also follow technology leaders on LinkedIn and Twitter to "
            "stay informed about industry opinions. Additionally, I take online courses on platforms like "
            "Coursera and Udemy to learn new skills. I believe that in the IT industry, continuous learning "
            "is not optional - it is essential for staying relevant and effective.'"
        ))
    q += 1

    pdf.add_question(q, "What are the qualities of a good team leader?",
        answer="Show understanding of effective leadership.",
        explanation=(
            "Example: 'A good team leader should have clear communication skills to ensure everyone "
            "understands goals and expectations. They should lead by example and be willing to do the "
            "hard work alongside their team. Empathy is crucial - understanding team members strengths, "
            "challenges, and motivations. A good leader delegates effectively, trusts their team, and "
            "gives credit where it is due. They also need to be decisive under pressure while remaining "
            "open to feedback. Most importantly, a good leader focuses on developing their team members "
            "and helping them grow, not just delivering results.'"
        ))
    q += 1

    pdf.add_question(q, "If you have two offers - TCS and another company - which would you choose?",
        answer="Choose TCS and give specific reasons.",
        explanation=(
            "Example: 'I would choose TCS because my decision is not based solely on compensation or "
            "brand name, but on long-term career growth. TCS offers unmatched exposure to diverse "
            "projects across global clients, a strong learning culture through ILP and continuous "
            "training programs, and the stability of being part of the Tata Group. The values that TCS "
            "upholds - integrity, respect for the individual, and excellence - align with my own values. "
            "I am looking for a place where I can build a meaningful career, and TCS is that place for me.'"
        ))
    q += 1

    pdf.add_question(q, "What would you do if you are unable to meet a project deadline?",
        answer="Show responsibility, communication, and problem-solving.",
        explanation=(
            "Example: 'If I realize I might miss a deadline, the first thing I would do is inform my "
            "manager proactively rather than waiting until the last moment. I would explain the situation, "
            "what I have completed so far, and what is remaining. I would also propose potential solutions "
            "- such as working extra hours, getting help from a colleague, or negotiating a slightly "
            "extended deadline for non-critical components. I believe transparency and early communication "
            "are crucial in such situations. Prevention is also important - I try to plan with buffer time "
            "and track progress regularly to avoid such scenarios.'"
        ))
    q += 1

    pdf.add_question(q, "How do you define teamwork?",
        answer="Show a nuanced understanding beyond just working together.",
        explanation=(
            "Example: 'Teamwork is more than just a group of people working together. It is about "
            "leveraging diverse strengths toward a shared goal while supporting each other through "
            "challenges. Good teamwork involves clear communication, mutual respect, shared accountability, "
            "and willingness to help others when they struggle. In my project experience, real teamwork "
            "happened when we moved beyond just dividing tasks and started actively collaborating - "
            "reviewing each others code, sharing knowledge, and stepping up when someone needed help. "
            "The result was always better than what any of us could have achieved alone.'"
        ))
    q += 1

    pdf.add_question(q, "What do you expect from the company?",
        answer="Focus on learning, growth, and fair treatment.",
        explanation=(
            "Example: 'From TCS, I expect a platform that supports my professional growth through "
            "challenging work and continuous learning opportunities. I expect a culture where merit is "
            "recognized and where I can receive constructive feedback to improve. I value a work "
            "environment that is collaborative, respectful, and inclusive. I also expect to be given "
            "opportunities to take on increasing responsibilities as I prove myself. From what I know "
            "about TCS, these are exactly the kind of values the company upholds, which is why I am "
            "eager to join.'"
        ))
    q += 1

    pdf.add_question(q, "Tell me about a time you failed.",
        answer="Be honest, show what you learned, and how you grew.",
        explanation=(
            "Example: 'In my third semester, I participated in a hackathon with high confidence. However, "
            "my team did not make it past the first round because we spent too much time on the idea "
            "and too little on implementation. We had a great concept but could not demonstrate a "
            "working prototype. That failure taught me the importance of execution over ideas. Since "
            "then, I always ensure I balance planning with action and set intermediate milestones to "
            "track progress. In my next hackathon, we finished in the top 5 by focusing on building "
            "a working MVP first and improving it iteratively.'"
        ))
    q += 1

    pdf.add_question(q, "Where do you see the IT industry heading in the next 10 years?",
        answer="Show awareness of technology trends.",
        explanation=(
            "Example: 'I believe the IT industry will be heavily shaped by AI and machine learning, "
            "cloud computing, cybersecurity, and quantum computing. AI is already transforming how "
            "businesses operate, and this will only accelerate. Cloud-native development will become the "
            "standard, and cybersecurity will grow even more critical as digital adoption increases. "
            "Companies like TCS that invest in innovation and upskilling their workforce will lead this "
            "transformation. For professionals, continuous learning will be the key to staying relevant "
            "in this rapidly evolving landscape.'"
        ))
    q += 1

    pdf.add_question(q, "Would you like to work in a startup or a large corporation?",
        answer="Show preference for large corporation (TCS) with good reasoning.",
        explanation=(
            "Example: 'At this stage of my career, I prefer a large corporation like TCS because it "
            "offers structured learning, mentorship from experienced professionals, and exposure to "
            "large-scale enterprise projects. In a large organization, I can learn industry best "
            "practices, understand how complex systems work, and build a strong professional foundation. "
            "TCS specifically offers the benefit of working with global clients across diverse domains, "
            "which will broaden my skills and perspective. While startups have their own appeal, I "
            "believe the learning infrastructure of a company like TCS is ideal for a fresher like me.'"
        ))
    q += 1

    pdf.add_tip("Always research the interviewer's name if possible and greet them by name.")
    pdf.add_tip("Practice your self-introduction in front of a mirror or record yourself to check body language.")
    pdf.add_tip("Keep all answers between 1-2 minutes. Avoid one-word answers and long monologues.")

    pdf.add_page_break()

    # =========================================================================
    # PART 2: BEHAVIORAL QUESTIONS (STAR Method)
    # =========================================================================
    pdf.add_topic_header("Part 2: Behavioral Questions - STAR Method",
                         "Behavioral questions assess how you have handled real situations in the past. "
                         "Use the STAR framework: Situation (set the scene), Task (explain your responsibility), "
                         "Action (describe what you did), Result (share the outcome). Each answer should be "
                         "specific, concise, and demonstrate positive qualities.")

    pdf.add_text("<b>The STAR Framework Explained:</b>")
    pdf.add_text("<b>S - Situation:</b> Briefly describe the context or background. When and where did this happen?")
    pdf.add_text("<b>T - Task:</b> What was your responsibility or what were you trying to achieve?")
    pdf.add_text("<b>A - Action:</b> What specific steps did you take? Focus on YOUR actions, not the team's.")
    pdf.add_text("<b>R - Result:</b> What was the outcome? Use numbers or specific details when possible.")
    pdf.add_tip("Prepare at least 5-6 stories from your college life that you can adapt to different behavioral questions.")

    bq = 1

    pdf.add_subtopic_header("2.1 Leadership & Initiative")

    pdf.add_question(bq, "Tell me about a time you demonstrated leadership.",
        answer="STAR Format",
        explanation=(
            "Situation: During my final year, our project team of four was struggling to make progress "
            "because there was no clear direction. Task: I stepped up to take the role of team coordinator, "
            "even though it was not formally assigned. Action: I organized our first proper planning "
            "meeting, created a project timeline with milestones, assigned roles based on each member's "
            "strengths, and set up weekly review meetings. I also created a shared document for tracking "
            "progress and blockers. Result: We went from being behind schedule to completing the project "
            "a week early. Our project received the highest grade in our section, and the professor "
            "praised our systematic approach."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a time when you took initiative beyond your responsibilities.",
        answer="STAR Format",
        explanation=(
            "Situation: During a group assignment in my fifth semester, I noticed that our college's "
            "study material repository was disorganized, making it difficult for juniors to find resources. "
            "Task: Although it was not my responsibility, I decided to organize the resources to help "
            "students across all years. Action: I spent two weekends categorizing study materials by "
            "subject and semester, created a shared Google Drive with proper folder structures, and wrote "
            "a simple index document. I also shared it on our college WhatsApp groups and asked "
            "contributors to follow a naming convention. Result: Over 200 students started using the "
            "repository within the first month. Several professors appreciated the effort and started "
            "uploading their own materials. It is still being maintained by juniors today."
        ))
    bq += 1

    pdf.add_question(bq, "Tell me about a time you motivated others.",
        answer="STAR Format",
        explanation=(
            "Situation: Before placement season, many of my classmates were anxious and unprepared. "
            "Task: I wanted to help create a supportive environment for placement preparation. "
            "Action: I organized an informal study group of 10 students. I created a schedule where "
            "we would practice aptitude questions daily, conduct mock interviews on weekends, and share "
            "useful resources in a group chat. I made it a point to celebrate small wins - when someone "
            "solved a tough problem, we acknowledged it. For students who were struggling, I paired "
            "them with stronger peers for one-on-one practice. Result: Eight out of ten students in "
            "our group got placed in the first round of placements, including two who had previously "
            "been very anxious about their prospects."
        ))
    bq += 1

    pdf.add_subtopic_header("2.2 Conflict Resolution & Difficult Situations")

    pdf.add_question(bq, "Describe a conflict you had with a team member and how you resolved it.",
        answer="STAR Format",
        explanation=(
            "Situation: During our mini project in the fifth semester, my teammate and I had a major "
            "disagreement about the technology stack. He wanted to use PHP, and I preferred Node.js. "
            "Task: We needed to resolve this quickly because it was holding up the entire project. "
            "Action: Instead of continuing to argue, I suggested we each spend one day building a "
            "small prototype of the same feature using our preferred technology. We would then compare "
            "them objectively based on performance, code readability, and team familiarity. I also "
            "listened carefully to his reasons for preferring PHP and acknowledged his valid points. "
            "Result: After comparing the prototypes, we found that Node.js was better suited for our "
            "real-time features, but his PHP prototype had cleaner routing. We went with Node.js "
            "and adopted some of his design patterns. The experience improved our working relationship "
            "and the final product was better for it."
        ))
    bq += 1

    pdf.add_question(bq, "Tell me about a time you dealt with a difficult person.",
        answer="STAR Format",
        explanation=(
            "Situation: In my project team, one member consistently missed deadlines and did not "
            "respond to group messages, which was affecting our overall progress. Task: As the team "
            "coordinator, I needed to address this without creating further conflict. Action: I "
            "had a private, one-on-one conversation with him instead of confronting him in front "
            "of the group. I learned he was dealing with family issues and was overwhelmed. I "
            "helped redistribute some of his tasks among the team for the immediate deadline and "
            "adjusted his responsibilities to smaller, more manageable chunks with closer check-ins. "
            "I also made sure he knew we supported him. Result: He gradually became more responsive "
            "and eventually caught up with his contributions. He later thanked me for understanding "
            "his situation rather than escalating the issue."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a situation where you had to work with someone you did not get along with.",
        answer="STAR Format",
        explanation=(
            "Situation: For a database lab assignment, I was paired with a classmate who had a very "
            "different working style - he preferred to do everything at the last minute, while I liked "
            "to plan ahead. Task: We needed to complete a complex database design and queries assignment "
            "within two weeks. Action: Instead of trying to change his working style, I adapted my "
            "approach. I did the initial database design and schema early and shared it with him. For "
            "the queries, I created a checklist of all requirements and suggested we split them equally "
            "with individual deadlines. I checked in mid-week without being pushy. Result: He appreciated "
            "the structure I provided and delivered his parts on time. We scored 90% on the assignment. "
            "I learned that adapting to different working styles is more productive than expecting others "
            "to change."
        ))
    bq += 1

    pdf.add_subtopic_header("2.3 Problem-Solving & Adaptability")

    pdf.add_question(bq, "Tell me about a time you solved a complex problem.",
        answer="STAR Format",
        explanation=(
            "Situation: During my final year project on face recognition, the system's accuracy dropped "
            "to below 70% in varying lighting conditions. Task: I needed to improve the accuracy to at "
            "least 90% for the project to be practically useful. Action: I researched image preprocessing "
            "techniques and implemented a pipeline that included histogram equalization, Gaussian blur "
            "for noise reduction, and adaptive thresholding. I also augmented our training data with "
            "images captured in different lighting conditions. I ran systematic experiments, changing "
            "one variable at a time and documenting results. Result: The accuracy improved to 95% in "
            "normal lighting and 88% in low light. My project guide was impressed with the methodical "
            "approach and used it as a reference for future batches."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a time when things did not go as planned.",
        answer="STAR Format",
        explanation=(
            "Situation: Our team had prepared for a college-level coding competition and were confident "
            "about winning. However, during the contest, the online judge had frequent server crashes. "
            "Task: We needed to adapt quickly and still perform our best despite the technical issues. "
            "Action: Instead of getting frustrated, I suggested we switch our strategy. We started "
            "working on solutions offline, testing them thoroughly before attempting to submit. I also "
            "helped my teammates stay calm and focused by reminding them that everyone was facing the "
            "same issues. We prioritized easier problems to maximize accepted solutions when the server "
            "was available. Result: While we did not win first place as expected, we finished third "
            "despite the disruptions. The organizers later acknowledged the technical issues and "
            "appreciated teams that handled them gracefully."
        ))
    bq += 1

    pdf.add_question(bq, "Tell me about a time you had to learn something quickly.",
        answer="STAR Format",
        explanation=(
            "Situation: In my final year project, the client-side requirement changed from a desktop "
            "application to a web application just three weeks before the submission deadline. "
            "Task: I needed to learn React.js from scratch and rebuild the entire frontend. "
            "Action: I created an intensive learning plan: Days 1-3 were for fundamentals through "
            "official React documentation and FreeCodeCamp. Days 4-7 were for building practice "
            "components similar to what I needed. Days 8-14 were for actual development. Days 15-21 "
            "were for testing and bug fixes. I also watched YouTube tutorials during meals and before "
            "bed. Result: I successfully delivered the React-based frontend two days before the deadline. "
            "The web version actually ended up being more user-friendly than the original desktop plan. "
            "This experience proved to me that structured learning under pressure can produce great results."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a situation where you had to adapt to a significant change.",
        answer="STAR Format",
        explanation=(
            "Situation: During the COVID-19 pandemic, our college shifted to online learning suddenly. "
            "All our lab sessions, project meetings, and even exams moved online. Task: I needed to adapt "
            "my study and project collaboration methods entirely. Action: I set up a structured daily "
            "routine to avoid the distractions of working from home. For our project team, I initiated "
            "daily video calls and set up a shared GitHub repository so we could collaborate on code "
            "effectively. I also explored new tools like Postman for API testing and Docker for "
            "consistent development environments across team members. Result: Our team actually became "
            "more productive than before because the forced remote collaboration made us document "
            "everything better and communicate more clearly. We submitted our project ahead of schedule "
            "and received excellent feedback."
        ))
    bq += 1

    pdf.add_subtopic_header("2.4 Failure & Learning")

    pdf.add_question(bq, "Tell me about your biggest failure and what you learned from it.",
        answer="STAR Format",
        explanation=(
            "Situation: In my third year, I attempted to build an ambitious mobile app for campus "
            "navigation as a side project. I planned to use AR (Augmented Reality) features. "
            "Task: I wanted to build and launch it within one semester. Action: I jumped straight into "
            "coding without proper planning or research. I chose technologies I was unfamiliar with, "
            "did not create wireframes or a project plan, and tried to build everything myself without "
            "seeking help. Result: After two months of frustration, I had to abandon the project because "
            "the scope was too large and my approach was flawed. What I learned: This failure taught me "
            "three critical lessons: (1) Always plan before coding, (2) Be realistic about scope and "
            "timeline, and (3) Seek help early when stuck. I applied these lessons to my final year "
            "project, which was a success because of proper planning and teamwork."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a time you received tough feedback. How did you respond?",
        answer="STAR Format",
        explanation=(
            "Situation: During a mock interview session organized by our placement cell, the interviewer "
            "gave me harsh feedback, saying my answers were too theoretical and lacked practical depth. "
            "Task: I needed to improve my interview skills before actual placements. Action: Instead of "
            "feeling discouraged, I took notes on all the feedback. I identified that my weakness was "
            "connecting theoretical concepts to real-world applications. I started practicing by "
            "explaining concepts with examples from my projects. I also participated in three more "
            "mock interviews over the next month and actively sought feedback each time. Result: By the "
            "time actual placements started, the same interviewer conducted another mock session and "
            "noted significant improvement. I cleared my very first placement interview. The experience "
            "taught me that tough feedback is a gift if you act on it."
        ))
    bq += 1

    pdf.add_question(bq, "Tell me about a mistake you made and how you fixed it.",
        answer="STAR Format",
        explanation=(
            "Situation: During my database project, I accidentally deleted a critical table from the "
            "production database while testing a cleanup script. Task: I needed to recover the data "
            "and ensure it did not happen again. Action: I immediately informed my project guide about "
            "the mistake instead of trying to hide it. I then checked if we had a recent backup and "
            "fortunately found one from the previous day. I restored the data and only lost one day's "
            "worth of test entries. More importantly, I implemented safeguards: I created a staging "
            "database for testing, added confirmation prompts for destructive queries, and set up "
            "automated daily backups. Result: The data was recovered with minimal loss, and the new "
            "safeguards prevented similar incidents for the rest of the project. My guide appreciated "
            "my honesty and the proactive prevention measures."
        ))
    bq += 1

    pdf.add_subtopic_header("2.5 Teamwork & Collaboration")

    pdf.add_question(bq, "Describe a time you helped a struggling team member.",
        answer="STAR Format",
        explanation=(
            "Situation: In my project team, one member was struggling with Java programming, which was "
            "essential for our backend development. His parts were consistently delayed. Task: The project "
            "timeline was at risk, and I needed to help him without making him feel incompetent. "
            "Action: I offered to do paired programming sessions with him after class, twice a week. "
            "Instead of doing his work for him, I guided him through the logic and helped him debug his "
            "own code. I also shared curated YouTube tutorials and practice problems suited to his level. "
            "I framed it as us working together rather than me teaching him. Result: Within three weeks, "
            "he was able to write and debug backend APIs independently. He went on to get placed at "
            "a reputed company and credited our sessions as a turning point. The experience reinforced "
            "my belief that patience and empathy are crucial in teamwork."
        ))
    bq += 1

    pdf.add_question(bq, "Tell me about a successful team project.",
        answer="STAR Format",
        explanation=(
            "Situation: In my sixth semester, our team participated in a 24-hour hackathon organized by "
            "a tech company. We were four team members with complementary skills. Task: We had to build "
            "a functional prototype for a healthcare management solution within 24 hours. Action: I took "
            "charge of the architecture and divided work: I handled the backend APIs, one member built "
            "the frontend, another managed the database, and the fourth worked on the presentation. "
            "We used Git for version control and had brief 30-minute sync meetings every 4 hours. When "
            "the frontend developer faced issues with API integration, I quickly created mock APIs so "
            "she could continue working in parallel. Result: We delivered a working prototype with user "
            "authentication, appointment booking, and a doctor dashboard. We won second place among 45 "
            "teams. The judges praised our clean code and effective teamwork."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a time when your team disagreed on an approach.",
        answer="STAR Format",
        explanation=(
            "Situation: During our major project, our team was split on whether to use a relational "
            "database (MySQL) or a NoSQL database (MongoDB). Two members strongly favored each option. "
            "Task: We needed to reach a consensus quickly to avoid delaying the project. Action: I "
            "proposed that we evaluate both options objectively. I created a comparison matrix with "
            "criteria relevant to our project: data structure complexity, query patterns, scalability "
            "needs, and our team's familiarity. Each member rated both options against each criterion. "
            "I also suggested we consider our project's specific data model, which had both structured "
            "and semi-structured components. Result: The evaluation clearly showed MySQL was better for "
            "our core transaction data, but we used MongoDB for storing logs and user activity data. "
            "This hybrid approach satisfied both camps and actually resulted in a better architecture."
        ))
    bq += 1

    pdf.add_subtopic_header("2.6 Time Management & Prioritization")

    pdf.add_question(bq, "Tell me about a time you managed multiple competing priorities.",
        answer="STAR Format",
        explanation=(
            "Situation: During my final semester, I had my project submission, three end-semester exams, "
            "and placement preparation all happening within the same month. Task: I needed to perform "
            "well in all three areas without compromising any. Action: I created a detailed four-week "
            "plan. I allocated mornings for placement preparation (aptitude and coding), afternoons for "
            "exam study, and evenings for project work. I identified overlap - my project used concepts "
            "from one of my exam subjects, so I studied them together. For placement prep, I focused on "
            "my weakest areas first. I also cut out social media and unnecessary activities for that "
            "month. Result: I scored above 8 CGPA in my exams, completed my project with an A grade, "
            "and got placed in the very first company that visited our campus. The key was planning "
            "ahead and being disciplined about following the schedule."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a time when you had to meet a tight deadline.",
        answer="STAR Format",
        explanation=(
            "Situation: Our project report submission deadline was moved up by one week due to a "
            "scheduling conflict with the external examiner's availability. Task: We had to complete "
            "the remaining testing, documentation, and report writing in half the expected time. "
            "Action: I immediately reorganized our task list by priority. I assigned the critical "
            "testing to two members who could work full-time, took on the report writing myself since "
            "I could write quickly, and asked the fourth member to handle diagrams and formatting. "
            "I set up a shared document so we could all contribute simultaneously. I also identified "
            "some non-essential features we could mark as future work to save time. Result: We "
            "submitted the report on time with all critical sections completed. The report quality "
            "was still good enough to earn us an A grade. The experience taught me that prioritization "
            "and parallel execution are key to meeting tight deadlines."
        ))
    bq += 1

    pdf.add_subtopic_header("2.7 Communication & Persuasion")

    pdf.add_question(bq, "Tell me about a time you had to explain something complex to someone non-technical.",
        answer="STAR Format",
        explanation=(
            "Situation: During my project presentation, the external examiner was from a management "
            "background and had limited technical knowledge about machine learning. Task: I needed to "
            "explain our face recognition algorithm in a way she could understand and evaluate. "
            "Action: I avoided technical jargon and used analogies. I compared the face recognition "
            "process to how humans recognize faces - we notice key features like the distance between "
            "eyes, nose shape, and face structure. I used the analogy of a lock and key to explain "
            "how the algorithm matches facial features. I also prepared visual diagrams showing the "
            "step-by-step process instead of showing code. Result: The examiner not only understood "
            "the concept but asked insightful follow-up questions. She gave us excellent marks for "
            "the presentation and specifically noted the clarity of explanation."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a time you had to persuade someone to see your point of view.",
        answer="STAR Format",
        explanation=(
            "Situation: In a group discussion during my college fest, I proposed using Python for a "
            "workshop instead of C++, but the organizing committee favored C++ because it was in the "
            "curriculum. Task: I needed to convince them that Python would attract more participants "
            "and be more practical. Action: I prepared data showing Python's growing industry demand, "
            "surveyed 50 students about their preferences, and created a comparison showing that Python "
            "workshops at other colleges had higher attendance. I presented this information calmly and "
            "also proposed a compromise: a Python workshop focused on real-world applications that "
            "would complement, not replace, the C++ curriculum knowledge. Result: The committee agreed "
            "to conduct the Python workshop. We had 85 participants, the highest for any workshop "
            "that year. The success led to Python being included in future fest events."
        ))
    bq += 1

    pdf.add_subtopic_header("2.8 Integrity & Ethics")

    pdf.add_question(bq, "Tell me about a time you had to stand up for what was right.",
        answer="STAR Format",
        explanation=(
            "Situation: During a group assignment, I discovered that one team member had copied a "
            "significant portion of code from the internet without attribution and was presenting it "
            "as original work. Task: I needed to address this without alienating the team member or "
            "jeopardizing our submission. Action: I had a private conversation with the member and "
            "explained the risks of plagiarism - both to our grades and our integrity. I offered to "
            "help him rewrite the code himself, using the online solution as a reference for logic "
            "but writing original code. We spent an evening rewriting the module together, and I helped "
            "him understand the logic. Result: We submitted original work that we could all be proud of. "
            "The team member appreciated my approach of helping rather than reporting, and he never "
            "repeated the practice. It reinforced my belief that integrity should never be compromised."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a time you went above and beyond what was expected.",
        answer="STAR Format",
        explanation=(
            "Situation: For our database management system project, the requirement was to build a simple "
            "student record management system with basic CRUD operations. Task: While the minimum "
            "requirement was straightforward, I wanted to deliver something that could actually be "
            "useful. Action: I added features beyond the requirement: a dashboard with analytics "
            "(attendance trends, grade distribution), automated email notifications for low attendance, "
            "a responsive design that worked on mobile devices, and role-based access control for "
            "different user types. I also wrote comprehensive documentation and created a user guide. "
            "Result: The professor was so impressed that he used our project as a demonstration for "
            "the next batch of students. He awarded us bonus marks and recommended us to a professor "
            "who was looking for students for a research project. Going the extra mile opened doors "
            "I had not even anticipated."
        ))
    bq += 1

    pdf.add_subtopic_header("2.9 Additional STAR Questions")

    pdf.add_question(bq, "Tell me about a time you had to work outside your comfort zone.",
        answer="STAR Format",
        explanation=(
            "Situation: I was asked to present our project at a state-level technical symposium. "
            "I had severe stage fright and had never presented to an audience larger than my classroom. "
            "Task: I needed to present our project confidently to an audience of 200+ people. "
            "Action: I practiced my presentation 15+ times, first alone, then in front of friends. "
            "I recorded myself and analyzed my body language and pacing. I joined a college speaking "
            "club for two weeks of intensive practice. On the day, I arrived early to familiarize "
            "myself with the stage and equipment. Result: While I was nervous initially, I delivered "
            "a 15-minute presentation that received a standing question round. We won the second-best "
            "project award. More importantly, I overcame a significant personal fear."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a creative solution you came up with for a problem.",
        answer="STAR Format",
        explanation=(
            "Situation: Our college WiFi was unreliable, and students frequently lost their work on "
            "cloud-based coding platforms during lab sessions. Task: We needed a way for students to "
            "code without depending on internet connectivity. Action: I proposed and implemented a "
            "lightweight local server using a Raspberry Pi that hosted an offline coding environment. "
            "I set up JupyterHub on it so that 30 students could simultaneously code through their "
            "browsers while connected to the local network without needing internet. I also added "
            "automatic backup to USB drives every 30 minutes. Result: The solution cost less than "
            "5000 rupees (the Raspberry Pi) and eliminated the internet dependency problem for our lab. "
            "The computer science department adopted this for three more labs. This taught me that "
            "creative solutions often come from constraints."
        ))
    bq += 1

    pdf.add_question(bq, "Tell me about a time you had to make a difficult decision.",
        answer="STAR Format",
        explanation=(
            "Situation: During our project, we were two weeks from submission and discovered that a "
            "core module built by a team member had significant bugs that would require a near-complete "
            "rewrite. Task: I had to decide whether to try patching the bugs or rewrite the module "
            "from scratch, which risked missing the deadline. Action: I analyzed both options objectively. "
            "Patching would be faster but would leave the system unstable. Rewriting would take more "
            "time but result in a reliable system. I chose to rewrite, working extra hours for a week. "
            "I also communicated the decision transparently to my team and professor. Result: We "
            "completed the rewrite four days before the deadline because the clean code was actually "
            "faster to develop than the patched version would have been. The module was bug-free in "
            "the final demo. Sometimes the harder decision is the right one."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a time when you received recognition for your work.",
        answer="STAR Format",
        explanation=(
            "Situation: In my third year, our department organized a code optimization challenge where "
            "students had to optimize existing slow programs. Task: I was given a data processing program "
            "that took 45 seconds to process a dataset and needed to optimize it. Action: I profiled "
            "the code to identify bottlenecks, implemented efficient data structures (replacing lists "
            "with hash maps for lookups), used algorithm optimization (reducing O(n^2) to O(n log n)), "
            "and added batch processing. I documented every optimization and its impact. Result: My "
            "optimized version processed the same dataset in 3 seconds - a 15x improvement. I won "
            "first place in the competition, and the department featured my solution in their annual "
            "report. The recognition was motivating, but the real reward was the deep understanding "
            "of performance optimization I gained."
        ))
    bq += 1

    pdf.add_question(bq, "Tell me about a time you had to balance quality with speed.",
        answer="STAR Format",
        explanation=(
            "Situation: During a hackathon, we had 24 hours to build a complete web application. "
            "Task: We needed to balance building features quickly with ensuring the code was functional "
            "and presentable. Action: I established a priority framework: must-have features first "
            "with basic error handling, nice-to-have features second, and polish last. I insisted "
            "on writing clean, modular code even under time pressure because messy code would slow "
            "us down later with bugs. I allocated the last 3 hours purely for testing and bug fixing "
            "rather than new features. Result: Our application had fewer features than some competitors "
            "but was the most stable during the demo. While others struggled with crashes, our demo "
            "was smooth. We won the 'Best Quality' special award. I learned that quality and speed "
            "are not always opposites - clean code is often faster in the long run."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a time you had to deal with ambiguity or unclear requirements.",
        answer="STAR Format",
        explanation=(
            "Situation: For our web development assignment, the professor gave very vague requirements: "
            "'Build a useful web application for students.' No specific features, technology, or scope "
            "were defined. Task: I needed to convert this ambiguous requirement into a concrete project "
            "plan. Action: I conducted a small survey among 30 classmates to identify their pain points. "
            "The most common issue was finding previous year question papers. I defined clear "
            "requirements: a searchable repository with upload/download capability, ratings, and "
            "subject-wise organization. I created wireframes and got the professor's approval before "
            "coding. Result: The application was well-received because it solved a real problem. "
            "The professor gave us extra marks for the structured approach to requirement gathering. "
            "I learned that when requirements are unclear, go to the users."
        ))
    bq += 1

    pdf.add_question(bq, "Tell me about a time you failed to meet expectations and how you recovered.",
        answer="STAR Format",
        explanation=(
            "Situation: I promised my project guide I would complete the API integration by a Monday "
            "but underestimated the complexity and could not deliver. Task: I needed to manage the "
            "situation honestly and recover quickly. Action: I emailed my guide on Saturday night, "
            "honestly explaining that I had underestimated the task. I outlined what was done (70%), "
            "what remained, and provided a realistic new timeline (Wednesday). I also identified why "
            "my estimate was wrong - I had not accounted for authentication complexity. I worked "
            "intensively over the next few days. Result: I delivered on Wednesday as promised. My "
            "guide appreciated the early, honest communication rather than excuses on Monday. He "
            "said the sign of a mature professional is not never failing, but communicating early "
            "and recovering reliably. I have applied this lesson to every commitment since."
        ))
    bq += 1

    pdf.add_question(bq, "Describe a time you improved a process or system.",
        answer="STAR Format",
        explanation=(
            "Situation: Our college's event registration was done through Google Forms, and organizers "
            "had to manually check for duplicates, send confirmation emails, and create attendance lists. "
            "Task: I saw an opportunity to automate this repetitive work. Action: I built a simple "
            "web application using Python Flask that handled event registration with automatic duplicate "
            "detection, email confirmations using SMTP, QR code generation for entry, and a real-time "
            "dashboard for organizers showing registration count and demographics. I deployed it on "
            "a free Heroku instance and trained the event committee on using it. Result: The system "
            "was used for 5 events that semester, handling over 500 registrations. It reduced the "
            "organizers workload by an estimated 10 hours per event and eliminated duplicate "
            "registrations entirely."
        ))
    bq += 1

    pdf.add_tip("For STAR answers, keep each section brief. The total answer should be 1-2 minutes.")
    pdf.add_tip("Always end with the Result - interviewers want to know the outcome, not just what you did.")
    pdf.add_tip("Quantify results whenever possible: numbers, percentages, time saved, etc.")

    pdf.add_page_break()

    # =========================================================================
    # PART 3: TECHNICAL DISCUSSION PREP
    # =========================================================================
    pdf.add_topic_header("Part 3: Technical Discussion Preparation",
                         "TCS HR interviews sometimes include light technical questions to gauge your "
                         "understanding. You are not expected to solve complex problems, but you should "
                         "be able to discuss your technical knowledge confidently.")

    pdf.add_subtopic_header("3.1 How to Explain Your Projects Effectively")

    pdf.add_text(
        "<b>Project Presentation Framework (Use this for every project):</b>"
    )
    pdf.add_text(
        "1. <b>Problem Statement (10 seconds):</b> What real-world problem does your project solve? "
        "Start with the WHY, not the WHAT."
    )
    pdf.add_text(
        "2. <b>Technology Stack (10 seconds):</b> Briefly mention the languages, frameworks, databases, "
        "and tools used. Example: 'Built with Python, Flask, MySQL, and deployed on AWS.'"
    )
    pdf.add_text(
        "3. <b>Your Role (15 seconds):</b> What specifically did YOU do? If it was a team project, "
        "clearly state your contribution."
    )
    pdf.add_text(
        "4. <b>Key Features (15 seconds):</b> Mention 2-3 standout features. Avoid listing everything."
    )
    pdf.add_text(
        "5. <b>Challenges & Solutions (15 seconds):</b> Mention one technical challenge and how you "
        "overcame it."
    )
    pdf.add_text(
        "6. <b>Outcome/Learning (10 seconds):</b> What was the result and what did you learn?"
    )

    pdf.add_tip("Practice your project explanation until it flows naturally in about 60-90 seconds.")
    pdf.add_tip("Always be prepared for follow-up questions like: Why did you choose this technology? "
                "What would you do differently? How would you scale this?")

    pdf.add_subtopic_header("3.2 Common Technical Follow-up Questions")

    pdf.add_text("<b>About Your Project:</b>")
    pdf.add_text("- Why did you choose [technology/language] for this project?")
    pdf.add_text("- What was the most challenging part of the project?")
    pdf.add_text("- How did you test your application?")
    pdf.add_text("- What would you improve if you had more time?")
    pdf.add_text("- How would you scale this for more users?")
    pdf.add_text("- Did you use any design patterns? Which ones and why?")
    pdf.add_text("- How did you handle errors/exceptions?")
    pdf.add_text("- What database design did you use and why?")

    pdf.add_text("<b>About Your Technical Skills:</b>")
    pdf.add_text("- What is the difference between Java and Python?")
    pdf.add_text("- Explain OOP concepts with examples from your project.")
    pdf.add_text("- What is the difference between SQL and NoSQL databases?")
    pdf.add_text("- What is version control? Have you used Git?")
    pdf.add_text("- Explain the SDLC (Software Development Life Cycle).")
    pdf.add_text("- What is Agile methodology?")
    pdf.add_text("- What is the difference between a stack and a queue?")
    pdf.add_text("- Explain any sorting algorithm and its time complexity.")

    pdf.add_subtopic_header("3.3 Branch-Wise Basics You Should Know")

    pdf.add_text("<b>Computer Science / IT:</b>")
    pdf.add_text("- OOP principles (Encapsulation, Inheritance, Polymorphism, Abstraction)")
    pdf.add_text("- Basic data structures (Array, Linked List, Stack, Queue, Tree, Graph)")
    pdf.add_text("- Database fundamentals (ACID properties, Normalization, Joins)")
    pdf.add_text("- Operating System basics (Process vs Thread, Deadlock, Memory management)")
    pdf.add_text("- Computer Network basics (OSI model, TCP/IP, HTTP vs HTTPS)")
    pdf.add_text("- SDLC models (Waterfall, Agile, Spiral)")

    pdf.add_text("<b>Electronics / Electrical / Mechanical / Civil (Non-CS):</b>")
    pdf.add_text("- You will likely NOT be asked deep technical questions from your branch for TCS IT roles.")
    pdf.add_text("- Focus on: Basic programming concepts, OOP basics, DBMS fundamentals, and SDLC.")
    pdf.add_text("- Be ready to explain why you want to work in IT despite a non-CS background.")
    pdf.add_text("- Mention any programming courses, certifications, or projects you have done.")
    pdf.add_text("- Show genuine interest and self-learning effort in software development.")

    pdf.add_tip("If asked something you do not know, say: 'I am not familiar with that topic, but I am "
                "eager to learn. In my experience, I have been able to pick up new concepts quickly.'")
    pdf.add_tip("Never bluff. Interviewers can easily catch it and it damages your credibility.")

    pdf.add_page_break()

    # =========================================================================
    # PART 4: QUESTIONS TO ASK THE INTERVIEWER
    # =========================================================================
    pdf.add_topic_header("Part 4: Questions to Ask the Interviewer",
                         "Always prepare 3-5 questions to ask the interviewer. It shows genuine interest "
                         "and engagement. Choose 2-3 from the list below based on the flow of your interview.")

    pdf.add_subtopic_header("4.1 About the Role & Work")
    pdf.add_text("1. What kind of projects are freshers typically assigned to in the first year?")
    pdf.add_text("2. What does a typical day look like for a new hire at TCS?")
    pdf.add_text("3. What technologies are currently in high demand within TCS projects?")
    pdf.add_text("4. How are freshers assigned to projects and business units?")
    pdf.add_text("5. What is the typical team size for projects?")

    pdf.add_subtopic_header("4.2 About Team & Culture")
    pdf.add_text("1. How would you describe the work culture at TCS?")
    pdf.add_text("2. How does TCS promote work-life balance?")
    pdf.add_text("3. What is the typical team structure for a project?")
    pdf.add_text("4. How does TCS foster collaboration among team members?")
    pdf.add_text("5. Are there opportunities for cross-functional or cross-domain projects?")

    pdf.add_subtopic_header("4.3 About Growth & Learning")
    pdf.add_text("1. Can you tell me more about the Initial Learning Program (ILP)?")
    pdf.add_text("2. What learning and development opportunities does TCS offer for freshers?")
    pdf.add_text("3. How does the performance evaluation process work for freshers?")
    pdf.add_text("4. What certifications does TCS encourage or sponsor?")
    pdf.add_text("5. What is the typical career growth path for someone joining as an Assistant Systems Engineer?")
    pdf.add_text("6. Are there opportunities to work on emerging technologies like AI, cloud, or blockchain?")

    pdf.add_subtopic_header("4.4 About TCS-Specific Programs")
    pdf.add_text("1. How long is the current ILP, and where is it conducted?")
    pdf.add_text("2. Does TCS have internal hackathons or innovation challenges for employees?")
    pdf.add_text("3. Can you tell me about TCS's global delivery model and opportunities for onsite exposure?")
    pdf.add_text("4. What is TCS's approach to employee wellness and mental health support?")
    pdf.add_text("5. How does TCS's internal job posting (IJP) system work for role changes?")

    pdf.add_tip("Do NOT ask about salary, leave policies, or working hours in the HR interview. "
                "These are details for after the offer.")
    pdf.add_tip("Do NOT ask questions whose answers are easily available on the TCS website.")
    pdf.add_tip("Listen to the answer carefully and ask a follow-up if appropriate - it shows genuine interest.")

    pdf.add_page_break()

    # =========================================================================
    # PART 5: DO'S AND DON'TS
    # =========================================================================
    pdf.add_topic_header("Part 5: Do's and Don'ts",
                         "The HR interview is as much about how you present yourself as what you say. "
                         "This section covers essential tips for making a strong impression.")

    pdf.add_subtopic_header("5.1 Body Language Tips")
    pdf.add_text("<b>Do:</b>")
    pdf.add_text("- Maintain natural eye contact with the interviewer (about 60-70% of the time).")
    pdf.add_text("- Sit upright with a slight forward lean - it shows engagement and interest.")
    pdf.add_text("- Smile naturally when greeting and during appropriate moments.")
    pdf.add_text("- Use hand gestures moderately to emphasize points.")
    pdf.add_text("- Nod occasionally to show you are actively listening.")
    pdf.add_text("- Keep your hands visible - on the table or your lap, not crossed or behind your back.")

    pdf.add_text("<b>Don't:</b>")
    pdf.add_text("- Avoid fidgeting with pen, hair, clothes, or any object.")
    pdf.add_text("- Do not slouch or lean back too casually.")
    pdf.add_text("- Avoid crossing your arms - it signals defensiveness.")
    pdf.add_text("- Do not look at the ceiling or floor while answering.")
    pdf.add_text("- Avoid excessive nodding or head movements.")
    pdf.add_text("- Do not touch your face repeatedly.")

    pdf.add_subtopic_header("5.2 Communication Tips")
    pdf.add_text("<b>Do:</b>")
    pdf.add_text("- Speak clearly and at a moderate pace. Do not rush.")
    pdf.add_text("- Use complete sentences, not one-word answers.")
    pdf.add_text("- Structure your answers with a beginning, middle, and end.")
    pdf.add_text("- Use specific examples instead of vague generalizations.")
    pdf.add_text("- Pause briefly before answering to collect your thoughts - it is better than rambling.")
    pdf.add_text("- Use positive language: say 'I am working on improving...' instead of 'I am bad at...'")
    pdf.add_text("- Thank the interviewer at the beginning and end.")

    pdf.add_text("<b>Don't:</b>")
    pdf.add_text("- Avoid filler words: 'um', 'uh', 'like', 'you know', 'basically'.")
    pdf.add_text("- Do not speak too fast or too slowly.")
    pdf.add_text("- Do not interrupt the interviewer.")
    pdf.add_text("- Avoid negative language about previous institutions, professors, or peers.")
    pdf.add_text("- Do not use slang or overly casual language.")
    pdf.add_text("- Do not memorize answers word-for-word - it sounds robotic.")
    pdf.add_text("- Avoid starting every answer with 'Actually...' or 'Basically...'")

    pdf.add_subtopic_header("5.3 Dress Code & Appearance")
    pdf.add_text("<b>Men:</b>")
    pdf.add_text("- Wear formal attire: light-colored shirt (white or light blue) with dark trousers.")
    pdf.add_text("- Tuck in your shirt. Wear a belt.")
    pdf.add_text("- Polished formal shoes (black or brown). Avoid sneakers or sandals.")
    pdf.add_text("- Clean-shaven or neatly trimmed beard.")
    pdf.add_text("- Neat, well-combed hair.")
    pdf.add_text("- Minimal accessories. A simple watch is fine.")
    pdf.add_text("- A tie is optional for fresher interviews but adds a professional touch.")

    pdf.add_text("<b>Women:</b>")
    pdf.add_text("- Wear formal attire: salwar kameez, formal kurti with trousers, or formal western wear.")
    pdf.add_text("- Avoid flashy colors or heavy patterns. Subtle, professional colors work best.")
    pdf.add_text("- Closed-toe formal footwear. Avoid high heels that are difficult to walk in.")
    pdf.add_text("- Minimal and professional jewelry. Avoid dangling earrings or heavy accessories.")
    pdf.add_text("- Neat hairstyle. If hair is long, tie it neatly.")
    pdf.add_text("- Light and natural makeup. Avoid heavy makeup.")

    pdf.add_text("<b>General:</b>")
    pdf.add_text("- Iron your clothes the night before.")
    pdf.add_text("- Carry a neat folder or bag with extra copies of your resume, certificates, and a pen.")
    pdf.add_text("- Use mild deodorant. Avoid strong perfumes or cologne.")
    pdf.add_text("- Clean and trimmed nails.")
    pdf.add_text("- Arrive 15-20 minutes early.")

    pdf.add_subtopic_header("5.4 Common Mistakes to Avoid")
    pdf.add_text("1. <b>Not researching TCS:</b> Not knowing basic facts about TCS is a major red flag.")
    pdf.add_text("2. <b>Badmouthing college/professors:</b> Never speak negatively about your institution.")
    pdf.add_text("3. <b>Lying about skills or experience:</b> If caught, it is an instant rejection.")
    pdf.add_text("4. <b>Over-confidence or arrogance:</b> There is a thin line between confidence and arrogance.")
    pdf.add_text("5. <b>Showing zero enthusiasm:</b> Monotone voice and flat expressions signal disinterest.")
    pdf.add_text("6. <b>Asking about salary in HR interview:</b> Wait for the offer stage.")
    pdf.add_text("7. <b>Not having questions to ask:</b> Saying 'No questions' shows lack of interest.")
    pdf.add_text("8. <b>Using your phone during waiting time:</b> You may be observed even before the interview.")
    pdf.add_text("9. <b>Providing inconsistent information:</b> Everything should match your resume.")
    pdf.add_text("10. <b>Not listening to the question properly:</b> Ask for clarification if needed, "
                 "rather than answering the wrong question.")

    pdf.add_subtopic_header("5.5 Things That Impress Interviewers")
    pdf.add_text("1. <b>Genuine enthusiasm:</b> A positive attitude and excitement about the opportunity.")
    pdf.add_text("2. <b>Self-awareness:</b> Knowing your strengths, weaknesses, and areas for improvement.")
    pdf.add_text("3. <b>Specific examples:</b> Backing up every claim with a concrete example.")
    pdf.add_text("4. <b>Knowledge about TCS:</b> Mentioning specific TCS initiatives, values, or recent news.")
    pdf.add_text("5. <b>Good questions:</b> Asking thoughtful questions that show genuine interest.")
    pdf.add_text("6. <b>Honesty:</b> Admitting what you do not know with a willingness to learn.")
    pdf.add_text("7. <b>Professional demeanor:</b> Polite, well-groomed, and respectful throughout.")
    pdf.add_text("8. <b>Clear communication:</b> Structured, concise answers without filler words.")
    pdf.add_text("9. <b>Growth mindset:</b> Showing how you have learned from failures and feedback.")
    pdf.add_text("10. <b>Long-term commitment:</b> Expressing genuine interest in building a career at TCS.")

    pdf.add_subtopic_header("5.6 Red Flags That Hurt Your Chances")
    pdf.add_text("1. Saying you have no weaknesses - it shows lack of self-awareness.")
    pdf.add_text("2. Mentioning you are only joining TCS as a backup plan.")
    pdf.add_text("3. Expressing unwillingness to relocate, work in shifts, or sign a bond.")
    pdf.add_text("4. Showing more interest in salary than learning.")
    pdf.add_text("5. Being unable to explain your own resume, projects, or skills.")
    pdf.add_text("6. Blaming others for failures or poor grades.")
    pdf.add_text("7. Appearing disinterested, bored, or distracted during the interview.")
    pdf.add_text("8. Making negative comments about the IT industry or TCS competitors.")
    pdf.add_text("9. Having clearly memorized scripted answers that do not match follow-up questions.")
    pdf.add_text("10. Being rude to reception staff, security, or other candidates (you are always being observed).")

    pdf.add_page_break()

    # =========================================================================
    # PART 6: TCS-SPECIFIC PREPARATION
    # =========================================================================
    pdf.add_topic_header("Part 6: TCS-Specific Preparation",
                         "Demonstrating knowledge about TCS shows genuine interest and preparation. "
                         "This section covers essential facts and information about TCS that every "
                         "candidate should know.")

    pdf.add_subtopic_header("6.1 TCS Values & Mission")
    pdf.add_text(
        "<b>TCS Mission:</b> To help customers achieve their business objectives by providing innovative, "
        "best-in-class consulting, IT solutions and services and to make it a joy for all stakeholders "
        "to work with us."
    )
    pdf.add_text(
        "<b>TCS Vision:</b> To be among the top 10 global companies by 2030 and to be the benchmark "
        "for technology-driven business transformation."
    )
    pdf.add_text("<b>Core Values of TCS (inherited from Tata Group):</b>")
    pdf.add_text("- <b>Integrity:</b> Conducting business fairly, with honesty and transparency.")
    pdf.add_text("- <b>Responsibility:</b> Integrating environmental and social principles into business.")
    pdf.add_text("- <b>Excellence:</b> Constantly striving to achieve the highest possible standards.")
    pdf.add_text("- <b>Pioneering:</b> Being bold and agile, courageously taking on challenges using "
                 "deep customer insight to develop innovative solutions.")
    pdf.add_text("- <b>Unity:</b> Working cohesively with colleagues across the group and with customers "
                 "and partners.")
    pdf.add_text("- <b>Respect for the Individual:</b> Treating everyone with dignity and valuing diversity.")

    pdf.add_tip("Mentioning TCS core values in your answers (especially Integrity, Excellence, and "
                "Learning) shows you have done your homework.")

    pdf.add_subtopic_header("6.2 Key Facts About TCS")
    pdf.add_table([
        ["Category", "Details"],
        ["Founded", "1968 by J.R.D. Tata"],
        ["Headquarters", "Mumbai, Maharashtra, India"],
        ["Parent Company", "Tata Sons (Tata Group)"],
        ["Current CEO & MD", "K Krithivasan (since June 2023)"],
        ["Chairman", "N Chandrasekaran (Tata Sons)"],
        ["Employees", "600,000+ across 55+ countries"],
        ["Revenue (FY 2024-25)", "Over $29 billion"],
        ["Market Cap", "Among the most valuable Indian companies"],
        ["Key Offices", "Mumbai, Chennai, Bengaluru, Hyderabad, Pune, Kolkata, and global offices"],
        ["Industry Rank", "India's largest IT company, among the world's top IT services firms"],
    ])

    pdf.add_subtopic_header("6.3 TCS Business Units & Services")
    pdf.add_text("<b>Major Service Lines:</b>")
    pdf.add_text("- <b>Consulting & Service Integration:</b> Business consulting, strategy, and advisory.")
    pdf.add_text("- <b>Cognitive Business Operations:</b> AI-powered business process services.")
    pdf.add_text("- <b>Cloud Infrastructure Services:</b> Cloud migration, management, and optimization.")
    pdf.add_text("- <b>Cybersecurity:</b> Threat management, compliance, and security consulting.")
    pdf.add_text("- <b>Enterprise Solutions:</b> SAP, Oracle, Microsoft, and Salesforce implementations.")
    pdf.add_text("- <b>IoT & Digital Engineering:</b> Product engineering and connected solutions.")
    pdf.add_text("- <b>TCS Interactive:</b> Design and creative services for digital experiences.")

    pdf.add_text("<b>Key Industry Verticals:</b>")
    pdf.add_text("- Banking, Financial Services, and Insurance (BFSI) - TCS's largest segment")
    pdf.add_text("- Retail and Consumer Goods")
    pdf.add_text("- Manufacturing")
    pdf.add_text("- Telecom, Media, and Technology")
    pdf.add_text("- Life Sciences and Healthcare")
    pdf.add_text("- Energy, Resources, and Utilities")
    pdf.add_text("- Government and Public Services")

    pdf.add_text("<b>Innovation Platforms:</b>")
    pdf.add_text("- <b>TCS Pace:</b> Innovation ecosystem connecting startups, academia, and technology partners.")
    pdf.add_text("- <b>TCS Research & Innovation:</b> Dedicated labs for AI, blockchain, IoT, and quantum computing.")
    pdf.add_text("- <b>TCS Ignio:</b> AI-powered automation platform for enterprise operations.")
    pdf.add_text("- <b>TCS BaNCS:</b> Core banking and financial services platform used by banks globally.")
    pdf.add_text("- <b>TCS iON:</b> Cloud-based platform for examinations, learning, and digital assessments.")

    pdf.add_subtopic_header("6.4 TCS ILP (Initial Learning Program)")
    pdf.add_text(
        "The Initial Learning Program (ILP) is TCS's flagship training program for freshers. Here is what "
        "you need to know:"
    )
    pdf.add_text("<b>Duration:</b> Approximately 45-60 days (varies by role and batch).")
    pdf.add_text("<b>Location:</b> Primarily at TCS training centers in Trivandrum (Technopark) or "
                 "Chennai, though virtual ILP has been conducted in recent years.")
    pdf.add_text("<b>What You Learn:</b>")
    pdf.add_text("- Programming fundamentals (Java, Python, or other languages based on project needs)")
    pdf.add_text("- Web technologies (HTML, CSS, JavaScript, frameworks)")
    pdf.add_text("- Database management (SQL, DBMS concepts)")
    pdf.add_text("- Software engineering practices (SDLC, Agile, testing)")
    pdf.add_text("- Soft skills (communication, presentation, email etiquette)")
    pdf.add_text("- Domain-specific training based on your assigned business unit")
    pdf.add_text("- TCS tools and internal platforms (Ultimatix, iEvolve, etc.)")

    pdf.add_text("<b>Assessment:</b>")
    pdf.add_text("- Regular tests and quizzes throughout the program")
    pdf.add_text("- Project work in teams")
    pdf.add_text("- Final assessment that determines your readiness for project deployment")
    pdf.add_text("- Performance in ILP can influence your initial project assignment")

    pdf.add_text("<b>Tips for ILP:</b>")
    pdf.add_text("- Take it seriously - your performance matters for project allocation.")
    pdf.add_text("- Network with fellow trainees - these will be your professional connections.")
    pdf.add_text("- Ask questions and participate actively in sessions.")
    pdf.add_text("- Use the time to build a strong foundation, especially if your background is non-CS.")

    pdf.add_subtopic_header("6.5 TCS Work Culture")
    pdf.add_text("<b>What to expect as a fresher at TCS:</b>")
    pdf.add_text(
        "- <b>Learning-oriented environment:</b> TCS heavily invests in employee upskilling. The iEvolve "
        "platform offers thousands of courses, and employees are encouraged to earn certifications."
    )
    pdf.add_text(
        "- <b>Diverse project exposure:</b> You may work across different technologies and domains "
        "throughout your career, gaining broad experience."
    )
    pdf.add_text(
        "- <b>Global opportunities:</b> TCS has offices in 55+ countries, and high performers can get "
        "onsite (international) assignments."
    )
    pdf.add_text(
        "- <b>Structured career path:</b> Clear progression from Assistant Systems Engineer to Systems "
        "Engineer to IT Analyst to Assistant Consultant and beyond."
    )
    pdf.add_text(
        "- <b>Work-life balance:</b> TCS promotes a healthy work-life balance with flexible work "
        "arrangements, wellness programs, and employee engagement activities."
    )
    pdf.add_text(
        "- <b>Internal mobility:</b> The Internal Job Posting (IJP) system allows employees to apply "
        "for different roles and projects within TCS."
    )
    pdf.add_text(
        "- <b>Community and CSR:</b> TCS encourages employees to participate in corporate social "
        "responsibility initiatives like TCS Maitree and volunteering programs."
    )

    pdf.add_subtopic_header("6.6 Recent TCS Achievements & News")
    pdf.add_text(
        "Stay updated with the latest TCS news before your interview. Here are some notable "
        "achievements to be aware of:"
    )
    pdf.add_text("- TCS consistently ranked among the world's most valuable IT brands.")
    pdf.add_text("- TCS crossed the $29 billion revenue milestone.")
    pdf.add_text("- TCS was recognized as a global top employer by the Top Employers Institute.")
    pdf.add_text("- TCS expanded its cloud and AI capabilities through strategic partnerships.")
    pdf.add_text("- TCS won multiple large deals across banking, insurance, and retail sectors.")
    pdf.add_text("- TCS continues to invest in sustainability and ESG (Environmental, Social, Governance) goals.")
    pdf.add_text("- TCS iON platform was used for conducting major national-level examinations.")

    pdf.add_tip("Before your interview, check the TCS website (tcs.com) and news sites for the "
                "most recent announcements and quarterly results.")
    pdf.add_tip("Mentioning a recent TCS achievement or initiative during your interview shows "
                "that you are genuinely interested and well-prepared.")

    pdf.add_page_break()

    # =========================================================================
    # FINAL TIPS & CHECKLIST
    # =========================================================================
    pdf.add_topic_header("Final Preparation Checklist",
                         "Use this checklist in the days leading up to your TCS HR interview.")

    pdf.add_text("<b>One Week Before:</b>")
    pdf.add_text("[ ] Research TCS thoroughly - values, services, recent news, CEO name")
    pdf.add_text("[ ] Prepare and practice your self-introduction (under 2 minutes)")
    pdf.add_text("[ ] Review all your projects and be ready to explain each in 60-90 seconds")
    pdf.add_text("[ ] Prepare 5-6 STAR stories that can be adapted to different behavioral questions")
    pdf.add_text("[ ] Practice answering common HR questions out loud (not just in your head)")
    pdf.add_text("[ ] Prepare 3-5 questions to ask the interviewer")
    pdf.add_text("[ ] Review your resume - be ready to explain every item on it")

    pdf.add_text("<b>One Day Before:</b>")
    pdf.add_text("[ ] Lay out your formal outfit and ensure it is clean and ironed")
    pdf.add_text("[ ] Print extra copies of your resume (2-3 copies)")
    pdf.add_text("[ ] Organize documents: resume, certificates, ID proof in a neat folder")
    pdf.add_text("[ ] Check the interview venue/platform details (time, location, or video call link)")
    pdf.add_text("[ ] Get a good night's sleep (7-8 hours minimum)")
    pdf.add_text("[ ] Do a final practice of your self-introduction")

    pdf.add_text("<b>On Interview Day:</b>")
    pdf.add_text("[ ] Eat a light, healthy meal before the interview")
    pdf.add_text("[ ] Arrive 15-20 minutes early")
    pdf.add_text("[ ] Turn off your phone before entering the interview room")
    pdf.add_text("[ ] Greet the interviewer with a smile and a confident handshake")
    pdf.add_text("[ ] Sit when invited to sit")
    pdf.add_text("[ ] Take a moment to think before answering each question")
    pdf.add_text("[ ] Thank the interviewer at the end")

    pdf.add_text("<b>For Virtual/Online Interviews:</b>")
    pdf.add_text("[ ] Test your internet connection, camera, and microphone beforehand")
    pdf.add_text("[ ] Choose a quiet, well-lit room with a neutral background")
    pdf.add_text("[ ] Dress formally from head to toe (not just the top half)")
    pdf.add_text("[ ] Look at the camera while speaking, not at the screen")
    pdf.add_text("[ ] Keep a glass of water nearby")
    pdf.add_text("[ ] Close all unnecessary tabs and applications")
    pdf.add_text("[ ] Have your resume open on screen for quick reference")

    pdf.add_tip("The HR interview is your chance to show who you are beyond your resume. Be authentic, "
                "be positive, and be yourself. Preparation builds confidence, and confidence makes a "
                "lasting impression. Good luck!")

    # Generate the PDF
    pdf.generate()
    return output_path


if __name__ == "__main__":
    path = build_pdf()
    print(f"HR Interview Guide PDF created at: {os.path.abspath(path)}")
