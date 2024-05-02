# AntidoteAI

Cyber security is used to protect and safeguard computers and various networks from ill-intended digital threats and attacks. It is getting more difficult in the information age due to the explosion of data and technology. There is a drastic rise in the new types of attacks where the conventional signature-based systems cannot keep up with these attacks. Additionally, the perpetual emergence of new malware strains further accentuates the inadequacy of signature-based solutions, as they rely on pre-existing knowledge. Machine learning seems to be a solution to solve many problems, including problems in cyber security. It is proven to be a very useful tool in the evolution of malware detection systems. 

In tandem with the challenges in malware detection, the ubiquity of phishing attacks poses a significant threat to individuals and organizations. Phishers continually refine their tactics, employing social engineering techniques and creating deceptive websites to pilfer sensitive information. Traditional methods, though valuable, struggle to keep pace with the evolving sophistication of these malicious activities. In response to these challenges, the introduction of machine learning into two critical features—PE file scanning and URL scanning—becomes imperative. The adaptability and learning capabilities of machine learning models enable them to stay ahead of the intricate strategies employed by phishers, offering a more resilient defense against deceptive practices. 

In this Tool, we delve into the integration of machine learning within PE file scanning and URL scanning, elucidating how these advancements can fortify malware and phishing detection capabilities. By harnessing the power of machine learning, we aim to address the shortcomings of conventional detection methods and usher in a new era of cybersecurity that is better equipped to combat the ever-evolving landscape of cyber threats. Beyond malware and phishing detection, our security tool incorporates indispensable features such as RAM-Booster, Junk Cleaner, and an Overall System Health Checker. This comprehensive suite evaluates not only Operating System health but also Network health, Hardware health, Application health, Resource health, Compliance health, and System updates. By seamlessly integrating these elements, our tool aims to provide a robust and user-friendly defense against evolving cyber threats, ensuring the resilience of digital ecosystems. 

## Getting Started

It has both Command-line Interface(engine.py) and UI(pretty.py)

## DATASET REQUIREMENTS 
The two data set that we have used in this project can be found in Kaggle.com While installing/running this project, the used does not need to install the module from Kaggle, it is already provided in the project file.
1. /PE/PEdata.csv
2. /URL/URLdataset.csv

##

### Installation

A step by step guide that will tell you how to get the development environment up and running.

```
$ git clone https://github.com/vaanshu/AntidoteAI.git

$ pip install -r requirements.txt

$ python engine.py

$ python pretty.py

```

## Organisation


![image](https://github.com/vaanshu/AntidoteAI-v2/assets/74679937/5bfb4569-6185-4e0f-a44d-dcfea5246163)



## Features Code Approach

## PE-SCANNER 
The core component of this feature centers around machine learning, where I implemented TPOT, a Python Automated Machine Learning tool designed to optimize machine learning pipelines through genetic programming. TPOT efficiently automates the laborious aspects of machine learning by intelligently exploring a multitude of potential pipelines to identify the most optimal one for the given dataset. In this instance, TPOT identified the best pipeline, and the **chosen classifier is XGB**. 

The dataset utilized in this analysis comprises 70.1% malware instances and 29.9% benign files. For data partitioning, I segregated the data into 70% training data and 30% testing data. Subsequently, I identified crucial features essential for classification using the extratrees.feature_importances_ function. Following this step, I preserved the XGB classifier and stored the pertinent features to retain essential information for future applications. 

 Post the machine learning phase, the project transitions to the file extraction segment, where I extract features necessary for classification. The primary challenge encountered during project development was extracting features from the PE Header file and storing them for the saved machine learning model. To address this, I utilized the pefile library (https://pypi.org/project/pefile/) for extracting the content of the PE Header. The selection of these features is executed using the "save selected features" approach, storing all critical features for the XGB classifier. The extraction of PE Header files is accomplished using the pefile library in Python, and the selected features are then input into the saved classifier model, facilitating predictions. If the file is identified as malicious, it undergoes quarantine. 

 

## URL-SCANNER
This feature centers on the utilization of a machine learning model to discern between phishing and legitimate URLs. To achieve this objective, I leveraged TPOT, a Python Automated Machine Learning tool renowned for optimizing machine learning pipelines through genetic programming. TPOT significantly simplifies the intricate process of machine learning by systematically exploring diverse pipelines to identify the most effective one tailored to a specific dataset. 

The dataset under investigation encompasses 11,054 rows, featuring 55.70% phishing URLs and 44.30% legitimate URLs across 32 distinct features. To ensure a robust evaluation, I partitioned the dataset into 20% testing data and 80% training data. 

Upon dataset partitioning, the subsequent step involved deploying TPOT to unearth the optimal machine learning pipeline. The outcome, as determined by TPOT, revealed the **GradientBoostingClassifier as the best-performing pipeline**, boasting an impressive accuracy rate of 96.92%. 

Having identified the optimal pipeline, I preserved the trained GradientBoostingClassifier as the model for prospective use. Additionally, I delved into comprehending the significance of various features within the dataset using the feature importances_ function. 

The project then transitioned to the feature extraction phase, where I extracted pertinent features essential for classification. Encountering challenges in feature extraction, I addressed this hurdle by employing a combination of URL parsing, HTTP requests, HTML parsing, WHOIS information, and specific heuristics. The features thus obtained were subsequently fed into the Classifier model, facilitating the prediction of the output. 

In summary, this research project seamlessly integrates TPOT for pipeline optimization, effectively handles dataset partitioning, identifies and preserves the optimal model, assesses feature importance, and implements a robust feature extraction process for accurate classification of phishing and legitimate URLs. 

 

## RAM-BOOSTER
In the rapidly evolving landscape of computing, the effective management of system resources remains a fundamental challenge. Among these resources, Random Access Memory (RAM) plays a pivotal role in ensuring optimal system performance. This research paper introduces a pioneering approach to address this challenge—an innovative RAM Booster enriched with artificial intelligence (AI) capabilities. The feature, encapsulated within the Tool’s framework, demonstrates intelligent decision-making tailored for dynamic RAM management. Two distinct options are presented: an AI-driven random process termination and a manual intervention mechanism. The former leverages AI algorithms to identify and terminate processes strategically, while the latter empowers users with manual control over specific process terminations. This paper explores the theoretical underpinnings and practical implications of the proposed AI-enhanced RAM Booster, aiming to contribute insights into the delicate balance between automated optimization and user-guided control in the intricate realm of system memory management. The AI feature is intended to be introduced in the future.  

## JUNK FILE FINDER
In the realm of digital file organization, maintaining an efficient and clutter-free storage environment is paramount for optimal system performance. This paper introduces a feature designed to enhance file management within a broader software tool—an advanced Junk File Remover. This feature, embedded seamlessly into the user interface, offers a comprehensive solution for identifying and eliminating unnecessary files that can accumulate over time. 

The Junk File Remover operates on a dual-pronged strategy. Firstly, it identifies duplicate files within a specified directory through the calculation of unique hash values using the MD5 algorithm. This process ensures a meticulous examination of the file structure, aiding in the reduction of redundant data. Secondly, the feature targets and removes files deemed as "junk," characterized by specific file extensions such as '.tmp', '.bak', '.log', and '.swp'. This proactive approach empowers users to maintain a lean and organized digital workspace. 

User interaction is a key component of this feature, as individuals are prompted to input a target directory for the file search. Additionally, the tool provides flexibility by allowing users to choose between checking for duplicate files or scanning for and removing junk files. This user-centric design emphasizes adaptability and customization, aligning the feature with diverse user preferences and file management needs. 

This paper explores the conceptual framework and practical implications of the introduced Junk File Remover feature. By addressing common challenges associated with file redundancy and clutter, this tool aims to streamline digital file management, contributing to a more organized and responsive computing experience. The subsequent sections will delve into the user interface, functionality details, and potential impact on enhancing overall system usability. 

## SYSTEM HEALTH CHECKER
Within the realm of digital systems, proactively monitoring and understanding the health of a computer is paramount. This introduction unveils a key feature designed to address this imperative—the System Health Checker. This integrated tool equips users with a diverse array of health-check functionalities, providing real-time insights into various aspects of their system's well-being. While the detailed workings of this feature are explored elsewhere, this introduction offers a broad overview of its capabilities and potential impact on system management. 

The System Health Checker encompasses distinct modules, each focusing on a specific facet of system health. From hardware and operating system status to network connectivity, application functionality, and compliance checks, this feature offers users a holistic perspective on their system's condition. Resource utilization metrics, such as CPU and memory usage, contribute to a nuanced understanding of performance dynamics. Additionally, the tool facilitates checks for critical updates, ensuring that the system remains current and secure. 

This introduction sets the stage for a deeper exploration of the System Health Checker feature. By consolidating diverse health-check functionalities within a single tool, users gain a centralized and user-friendly means to monitor and maintain their system's integrity. Subsequent sections will delve into the individual health-check modules, user interaction, and the broader implications of integrating such a feature into system management. 

## COMMAND LINE INTERFACE

![image](https://github.com/vaanshu/AntidoteAI-v2/assets/74679937/ffd92a9c-982e-4e0f-982c-9a54333ea9ad)


## UI 

![image](https://github.com/vaanshu/AntidoteAI-v2/assets/74679937/d4392010-67a5-4ee7-b3f1-20cc092988c7)


## RESULT 

The presented tool addresses the escalating challenges in cybersecurity by leveraging machine learning in the realms of malware and phishing detection. The **PE-Scanner, utilizing TPOT-optimized XGBoost Classifier, demonstrates exceptional performance in identifying and quarantining malicious files, achieving an impressive accuracy of 98.45%**. Similarly, the **URL-Scanner, employing TPOT and GradientBoostingClassifier, showcases a robust defense against phishing attacks, with a classification accuracy of 97.4%**. 

Beyond cybersecurity threats, the tool extends its capabilities to enhance overall system health and performance. The RAM-Booster efficiently manages system resources, presenting both AI-driven and manual intervention options for dynamic RAM management. The Junk File Remover contributes to digital file organization by identifying and eliminating duplicate and unnecessary files, promoting a clutter-free environment. 

The System Health Checker consolidates diverse health-check functionalities, providing real-time insights into various aspects of system well-being. This comprehensive suite evaluates not only operating system health but also network, hardware, application, resource, compliance health, and system updates. 

While the AI-based RAM Booster is yet to be implemented, the tool, as a whole, integrates seamlessly into user interfaces, emphasizing adaptability and customization. The presented research and its results underscore the significance of incorporating machine learning into cybersecurity tools, paving the way for a more resilient defense against the ever-evolving landscape of cyber threats and contributing to a streamlined and responsive computing experience. 

