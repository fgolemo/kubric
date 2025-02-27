#!/bin/bash -x

DATASET_NAME=${1}  # has to be the same as the filename of DATASET_CONFIG
DATASET_CONFIG="kubric/datasets/${DATASET_NAME}.py"
GCP_PROJECT=kubric-xgcp
GCS_BUCKET=gs://research-brain-kubric-xgcp
REGION=us-central1
JOB_NAME=${2}
MACHINE_TYPE="n1-highmem-32"
NUM_WORKERS=20

# create a pseudo-package in a temporary directory to ship the dataset code to dataflow workers
# https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/
TEMP=$(mktemp -d)
mkdir "$TEMP/$DATASET_NAME"
cp "$DATASET_CONFIG" "$TEMP/$DATASET_NAME/__init__.py"
echo "Dummy package to ship dataset code to worker nodes" > "$TEMP/README"
cat > "$TEMP/setup.py" <<EOF
import setuptools

setuptools.setup(
    name='$DATASET_NAME',
    version='0.0.1',
    url="https://github.com/google-research/kubric",
    author="kubric authors",
    author_email="kubric@google.com",
    install_requires=['tensorflow_datasets', 'pypng', 'imageio'],
    packages=setuptools.find_packages(),
)
EOF

# install_requires=[
#        'tensorflow_datasets @ git+https://git@github.com/qwlouse/datasets@master#egg=tensorflow_datasets'],

#
tfds build $DATASET_CONFIG \
  --data_dir=$GCS_BUCKET/tensorflow_datasets \
  --beam_pipeline_options="runner=DataflowRunner,project=$GCP_PROJECT,job_name=$JOB_NAME,\
staging_location=$GCS_BUCKET/binaries,temp_location=$GCS_BUCKET/temp,region=$REGION,\
setup_file=$TEMP/setup.py,machine_type=$MACHINE_TYPE,num_workers=$NUM_WORKERS,experiments=upload_graph"



# clean-up: delete the pseudo-package
rm -rf "$TEMP"
