# E-commerce Platform Integrations

## PLATFORM-SPECIFIC PACKAGES

### GUMROAD (Primary)
```bash
zip -r gumroad-package.zip course/ marketing/ assessments/ LICENSE.txt
# Upload single ZIP + thumbnail
```

### ETSY DIGITAL PRODUCT
```
5 gallery images + ZIP + instruction PDF
Price: $27-47
Keywords: [topic] course, [skill] tutorial, digital download
```

### TEACHABLE LMS IMPORT
```
/teachable/
├── course.json (LMS manifest)
├── modules/ (individual ZIPs)
├── quizzes/ (JSON)
└── assets/
```

## AUTOMATION SCRIPTS
```bash
#!/bin/bash
# setup_gumroad.sh
cp -r delivery/gumroad/* /tmp/gumroad-upload/
```

## LICENSE SYSTEM
- PDF license generator
- Unique keys per purchase
- Update checker

## DELIVERY FOLDER
/delivery/
├── gumroad/
├── etsy/
├── teachable/
└── generic/
