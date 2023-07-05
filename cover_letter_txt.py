from datetime import date

def cover_letter_txt(choice, role, company, skill_1, skill_2, cover_letter_txt_path):

    with open(cover_letter_txt_path, 'w') as f:

        f.write(f"Dear Hiring Manager,")

        # ----- PARAGRAPH 1 - BELIEF HOOK AND PURPOSE -----
        f.write(f"\n\nIn today's fast-paced business environment, data-driven decision making is crucial for driving growth, efficiency, and innovation. As a highly skilled individual with expertise in {skill_1} and {skill_2}, I am excited to apply for a {role} position at {company}")
        
        # ----- PARAGRAPH 2 - PERSONAL TOUCH -----
        f.write(f".\n\nMy insightful discussions with 3 employees reinforced my interest in joining the {company} family. The thing that impressed me the most during the interactions was their high level of enthusiasm. It was clear that they all felt a strong sense of ownership and pride in the outcomes of their work.\n\n")

        # ----- PARAGRAPH 3 - KEY SKILLS -----
        f.write(f"With over 2 years of experience in the data sphere, I strongly believe that I have developed three crucial abilities that will help me excel in this challenging role:\n\n")

        # Data Analyst
        if choice == '1':
            # Advanced Analytics
            f.write(f"1. Advanced Analytics: Currently, as a Data Scientist at UbiLab and formerly with Research Groups at Vienna University of Technology and NYU Abu Dhabi, I have actively been engaged in cleaning, preprocessing, and interpreting large time-series datasets to extract meaningful insights and conclusions. With my strong programming skills, I can enable the team by automating tasks, saving time and resources, and helping them make informed decisions based on trends and patterns.\n\n")

            # Data Visualization
            f.write(f"2. Data Visualization: In previous roles, I have honed my skills in creating visually compelling and informative data visualizations. By leveraging industry-leading tools and technologies, I excel at transforming complex datasets into clear and actionable insights. Whether it's designing interactive dashboards, crafting intuitive charts, or employing effective data storytelling techniques, I am adept at presenting information in a visually appealing and easily understandable manner. This expertise will surely enable {company} to derive valuable insights, make informed decisions, and drive business growth.\n\n")

        # Data Scientist
        if choice == '2':
            # Advanced Analytics
            f.write(f"1. Advanced Analytics: Currently, as a Data Scientist at UbiLab and formerly with Research Groups at Vienna University of Technology and NYU Abu Dhabi, I have actively been engaged in cleaning, preprocessing, and interpreting large time-series datasets to extract meaningful insights and conclusions. With my strong programming skills, I can enable the team by automating tasks, saving time and resources, and helping them make informed decisions based on trends and patterns.\n\n")

            # AI & Machine Learning
            f.write(f"2. AI & Machine Learning: Due to my experience as a Machine Learning Researcher at the University of Waterloo, Vienna University of Technology, and NYU Abu Dhabi, I possess expertise in designing and implementing end-to-end ML solutions that encompass feature engineering, model selection, tuning, and the identification of key performance metrics. With proficiency in ML tools and frameworks, I can empower an organization like {company} to achieve significant improvements in productivity, revenue, and competitiveness.\n\n")

        # ML Engineer
        if choice == '3':
            # Advanced Analytics
            f.write(f"1. Advanced Analytics: Currently, as a Data Scientist at UbiLab and formerly with Research Groups at Vienna University of Technology and NYU Abu Dhabi, I have actively been engaged in cleaning, preprocessing, and interpreting large time-series datasets to extract meaningful insights and conclusions. With my strong programming skills, I can enable the team by automating tasks, saving time and resources, and helping them make informed decisions based on trends and patterns.\n\n")

            # AI & Machine Learning
            f.write(f"2. AI & Machine Learning: Due to my experience as a Machine Learning Researcher at the University of Waterloo, Vienna University of Technology, and NYU Abu Dhabi, I possess expertise in designing and implementing end-to-end ML solutions that encompass feature engineering, model selection, tuning, and the identification of key performance metrics. With proficiency in ML tools and frameworks, I can empower an organization like {company} to achieve significant improvements in productivity, revenue, and competitiveness.\n\n")

        # MLOps Engineer
        if choice == '4':
            # Advanced Analytics
            f.write(f"1. Scalable Data Pipelines and Automation: Currently, as a ML Engineer at UbiLab and formerly with Research Groups at Vienna University of Technology and NYU Abu Dhabi, I have actively been involved in developing and maintaining scalable and efficient data pipelines for cleaning, preprocessing, and interpreting large time-series datasets. By leveraging my strong programming skills and expertise in infrastructure technologies and DevOps practices, I can enable the team by automating tasks, streamlining processes, and optimizing resource utilization. This not only saves time and resources but also facilitates informed decision-making based on trends and patterns.\n\n")

            # End-to-End ML Solutions and Infrastructure Management
            f.write(f"2. End-to-End ML Solutions and Infrastructure Management: Due to my experience as in MLOps at the University of Waterloo, Vienna University of Technology, and NYU Abu Dhabi, I possess expertise in designing and implementing end-to-end ML solutions that encompass feature engineering, model selection, tuning, and the establishment of key performance metrics. Alongside my proficiency in ML tools and frameworks, I also bring a strong understanding of infrastructure technologies and DevOps principles. This enables me to effectively deploy and manage ML models and systems, ensuring scalability, reliability, and efficient utilization of computing resources. By leveraging my skills and knowledge, I can contribute to significant improvements in productivity, revenue, and competitiveness for an organization like {company}.\n\n")

        # Data Engineer
        if choice == '5':
            # Big Data & Data Engineering
            f.write(f"1. Big Data & Data Engineering: Due to my experience in big data at the University of Waterloo, Vienna University of Technology, and NYU Abu Dhabi, I possess expertise in building and maintaining scalable data infrastructures and distributed systems. I have hands-on experience with technologies such as Hadoop, Spark, and Kafka, enabling efficient processing and analysis of large volumes of data. With my skills in data modeling, data warehousing, and ETL (Extract, Transform, Load) processes, I can help {company} leverage big data technologies to unlock valuable insights, improve data accessibility, and drive data-centric strategies.\n\n")

            # Advanced Analytics
            f.write(f"2. Advanced Analytics: Currently, as a Data Engineer at UbiLab and formerly with Research Groups at Vienna University of Technology and NYU Abu Dhabi, I have actively been involved in designing and implementing scalable data processing systems for cleaning, transforming, and analyzing large time-series datasets. With my strong programming and data manipulation skills, I can contribute to the team by developing efficient data pipelines, optimizing data storage and retrieval, and ensuring data quality and integrity. These efforts facilitate the extraction of valuable insights and facilitate data-driven decision-making.\n\n")


        # Communication and Leadership
        f.write("3. Communication & Leadership: Strong communication skills allow me to clearly articulate complex technical concepts to non-technical stakeholders and effectively collaborate with cross-functional teams. My leadership skills enable me to guide and mentor team members, while also setting the direction and priorities for projects. Being an active member of Toastmasters International and mentoring more than 10 undergraduates as a Mitacs Globalink Mentor at the University of Waterloo has allowed me to further consolidate this skill.\n\n")

        f.write(f"Thank you for taking the time to review my application. My work experiences, coupled with my affinity for this role would make me an asset for {company}. I look forward to speaking with you in further detail about the available position.")

    return None