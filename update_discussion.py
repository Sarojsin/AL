import json

files = [
    (r'E:\semister_notes\sixsemister\AI\Lab\Logistic_Regression.ipynb', True),
    (r'E:\semister_notes\sixsemister\AI\Lab\heart_disease_logistic_classifier.ipynb', True),
    (r'E:\semister_notes\sixsemister\AI\Lab\Linear_Regression.ipynb', False),
]

for fp, has_separate_conclusion in files:
    with open(fp, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    cells = nb['cells']

    # Replace/insert simple Discussion and Conclusion blocks
    new_discussion = [
        '### Discussion\n',
        '\n',
        'In this lab I worked with two versions of the same prediction task: one using a single feature and one using many features together.\n',
        '\n',
        'For the single-feature model, the idea was simple: see how well one variable, like cholesterol or years of experience, could predict the target on its own. This helped me understand what a basic model looks like and how to read its output.\n',
        '\n',
        'Using multiple features made the model stronger because it had more information to learn from. The accuracy and recall improved, which showed that adding the right features does help the model make better predictions.\n',
        '\n',
        'I also noticed that single-feature models are easier to explain, but they often miss important patterns. Multi-feature models can capture more of those patterns, even if they are a bit harder to interpret.\n',
        '\n',
        'Overall, this exercise helped me see why we follow a pipeline: loading data, cleaning it, selecting features, training the model, and then checking how well it performed.\n',
    ]
    if has_separate_conclusion:
        new_conclusion = [
            '### Conclusion\n',
            '\n',
            'This lab successfully covered the main steps of a basic ML workflow.\n',
            '\n',
            'I learned how Logistic Regression is used for classification and how Linear Regression is used for predicting continuous values like salary.\n',
            '\n',
            'The key takeaway is that more informative features usually lead to better results, but simpler models are still useful for understanding how the algorithm works.\n',
        ]

    # Find and replace discussion/conclusion cells
    final_cells = []
    i = 0
    while i < len(cells):
        cell = cells[i]
        src = ''.join(cell.get('source', []))
        if cell.get('cell_type') == 'markdown' and 'DISCUSSION' in src.upper():
            final_cells.append({
                'cell_type': 'markdown',
                'metadata': cell.get('metadata', {}),
                'source': new_discussion,
            })
            i += 1
            continue
        if cell.get('cell_type') == 'markdown' and 'CONCLUSION' in src.upper():
            if has_separate_conclusion:
                final_cells.append({
                    'cell_type': 'markdown',
                    'metadata': cell.get('metadata', {}),
                    'source': new_conclusion,
                })
                i += 1
                continue
        final_cells.append(cell)
        i += 1

    nb['cells'] = final_cells

    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print('Updated:', fp.split('\\')[-1])
