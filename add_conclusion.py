import json

fp = r'E:\semister_notes\sixsemister\AI\Lab\Linear_Regression.ipynb'

conclusion_md = [
    '### Conclusion\n',
    '\n',
    'In this lab I completed a basic machine learning workflow using Linear Regression.\n',
    '\n',
    'I started by loading the dataset, checked for missing values, selected the input feature, trained the model, and evaluated it using MSE and R² score.\n',
    '\n',
    'Using multiple features helped improve the prediction compared to using just one feature, which taught me how feature selection affects model performance.\n',
    '\n',
    'This lab also helped me understand what the coefficients and intercept mean in a regression model, and how to read evaluation metrics in a simple way.\n',
    '\n',
    'Overall, this was a good starting point for understanding how machine learning models are trained and tested on real data.\n',
]

with open(fp, 'r', encoding='utf-8') as f:
    nb = json.load(f)

nb['cells'].append({
    'cell_type': 'markdown',
    'metadata': {},
    'source': conclusion_md,
})

with open(fp, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Added conclusion to', fp.split('\\')[-1])
