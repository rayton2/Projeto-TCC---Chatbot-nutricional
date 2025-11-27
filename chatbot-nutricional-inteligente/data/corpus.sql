-- Schema for the knowledge base
CREATE TABLE IF NOT EXISTS knowledge_base (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sample data for the knowledge base
INSERT INTO knowledge_base (question, answer) VALUES
('What is a balanced diet?', 'A balanced diet includes a variety of foods in the right proportions.'),
('How much water should I drink daily?', 'It is recommended to drink at least 2 liters of water a day.'),
('What are the benefits of eating fruits and vegetables?', 'Fruits and vegetables are rich in vitamins, minerals, and fiber, which are essential for good health.');