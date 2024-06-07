{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3ace63ab-ecba-4f67-b98d-49fde099feba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlitNote: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "  Downloading streamlit-1.35.0-py2.py3-none-any.whl (8.6 MB)\n",
      "     ---------------------------------------- 8.6/8.6 MB 707.8 kB/s eta 0:00:00\n",
      "Collecting rich<14,>=10.14.0\n",
      "  Downloading rich-13.7.1-py3-none-any.whl (240 kB)\n",
      "     -------------------------------------- 240.7/240.7 kB 1.3 MB/s eta 0:00:00\n",
      "Collecting blinker<2,>=1.0.0\n",
      "  Downloading blinker-1.8.2-py3-none-any.whl (9.5 kB)\n",
      "Collecting altair<6,>=4.0\n",
      "  Downloading altair-5.3.0-py3-none-any.whl (857 kB)\n",
      "     ------------------------------------ 857.8/857.8 kB 935.5 kB/s eta 0:00:00\n",
      "Requirement already satisfied: packaging<25,>=16.8 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from streamlit) (21.3)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from streamlit) (1.4.4)\n",
      "Collecting tenacity<9,>=8.1.0\n",
      "  Downloading tenacity-8.3.0-py3-none-any.whl (25 kB)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from streamlit) (6.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from streamlit) (9.2.0)\n",
      "Collecting pyarrow>=7.0\n",
      "  Downloading pyarrow-16.1.0-cp310-cp310-win_amd64.whl (25.9 MB)\n",
      "     -------------------------------------- 25.9/25.9 MB 921.8 kB/s eta 0:00:00\n",
      "Collecting toml<2,>=0.10.1\n",
      "  Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)\n",
      "Collecting pydeck<1,>=0.8.0b4\n",
      "  Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
      "     ---------------------------------------- 6.9/6.9 MB 1.1 MB/s eta 0:00:00\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from streamlit) (4.3.0)\n",
      "Collecting protobuf<5,>=3.20\n",
      "  Downloading protobuf-4.25.3-cp310-abi3-win_amd64.whl (413 kB)\n",
      "     ------------------------------------ 413.4/413.4 kB 955.4 kB/s eta 0:00:00\n",
      "Collecting cachetools<6,>=4.0\n",
      "  Downloading cachetools-5.3.3-py3-none-any.whl (9.3 kB)\n",
      "Collecting watchdog>=2.1.5\n",
      "  Downloading watchdog-4.0.1-py3-none-win_amd64.whl (83 kB)\n",
      "     -------------------------------------- 83.0/83.0 kB 667.5 kB/s eta 0:00:00\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from streamlit) (1.23.1)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from streamlit) (2.28.1)\n",
      "Collecting gitpython!=3.1.19,<4,>=3.0.7\n",
      "  Downloading GitPython-3.1.43-py3-none-any.whl (207 kB)\n",
      "     ------------------------------------ 207.3/207.3 kB 360.3 kB/s eta 0:00:00\n",
      "Requirement already satisfied: jinja2 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.0.3)\n",
      "Collecting toolz\n",
      "  Downloading toolz-0.12.1-py3-none-any.whl (56 kB)\n",
      "     -------------------------------------- 56.1/56.1 kB 245.4 kB/s eta 0:00:00\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.16.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.5)\n",
      "Collecting gitdb<5,>=4.0.1\n",
      "  Downloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
      "     ---------------------------------------- 62.7/62.7 kB 1.1 MB/s eta 0:00:00\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from packaging<25,>=16.8->streamlit) (3.0.9)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2022.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from requests<3,>=2.27->streamlit) (1.26.11)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2022.9.24)\n",
      "Collecting markdown-it-py>=2.2.0\n",
      "  Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)\n",
      "     ---------------------------------------- 87.5/87.5 kB 1.6 MB/s eta 0:00:00\n",
      "Collecting pygments<3.0.0,>=2.13.0\n",
      "  Downloading pygments-2.18.0-py3-none-any.whl (1.2 MB)\n",
      "     ---------------------------------------- 1.2/1.2 MB 317.4 kB/s eta 0:00:00\n",
      "Collecting smmap<6,>=3.0.1\n",
      "  Downloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (21.4.0)\n",
      "Collecting mdurl~=0.1\n",
      "  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\user\\anaconda3\\envs\\sehmilo\\lib\\site-packages (from python-dateutil>=2.8.1->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Installing collected packages: watchdog, toolz, toml, tenacity, smmap, pygments, pyarrow, protobuf, mdurl, cachetools, blinker, pydeck, markdown-it-py, gitdb, rich, gitpython, altair, streamlit\n",
      "  Attempting uninstall: tenacity\n",
      "    Found existing installation: tenacity 8.0.1\n",
      "    Uninstalling tenacity-8.0.1:\n",
      "      Successfully uninstalled tenacity-8.0.1\n",
      "  Attempting uninstall: pygments\n",
      "    Found existing installation: Pygments 2.11.2\n",
      "    Uninstalling Pygments-2.11.2:\n",
      "      Successfully uninstalled Pygments-2.11.2\n",
      "Successfully installed altair-5.3.0 blinker-1.8.2 cachetools-5.3.3 gitdb-4.0.11 gitpython-3.1.43 markdown-it-py-3.0.0 mdurl-0.1.2 protobuf-4.25.3 pyarrow-16.1.0 pydeck-0.9.1 pygments-2.18.0 rich-13.7.1 smmap-5.0.1 streamlit-1.35.0 tenacity-8.3.0 toml-0.10.2 toolz-0.12.1 watchdog-4.0.1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
      "dash 1.19.0 requires dash-core-components==1.15.0, but you have dash-core-components 1.3.1 which is incompatible.\n",
      "dash 1.19.0 requires dash-html-components==1.1.2, but you have dash-html-components 1.0.1 which is incompatible.\n",
      "dash 1.19.0 requires dash-renderer==1.9.0, but you have dash-renderer 1.1.2 which is incompatible.\n",
      "dash 1.19.0 requires dash-table==4.11.2, but you have dash-table 4.4.1 which is incompatible.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "fcf1ed5b",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_10996\\118411577.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mplotly\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexpress\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpx\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mcategory_encoders\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mOneHotEncoder\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlinear_model\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mRidge\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "from category_encoders import OneHotEncoder\n",
    "from sklearn.linear_model import Ridge\n",
    "from sklearn.metrics import mean_absolute_error\n",
    "from sklearn.pipeline import make_pipeline\n",
    "\n",
    "# Function to wrangle data\n",
    "def wrangle(file):\n",
    "    df = pd.read_csv(file)\n",
    "    return df\n",
    "\n",
    "# Streamlit app\n",
    "st.title(\"Interactive Data Visualization for Borehole Exploration\")\n",
    "\n",
    "# File uploader\n",
    "st.sidebar.subheader(\"Upload your data\")\n",
    "uploaded_file = st.sidebar.file_uploader(\"Choose a CSV file\", type=\"csv\")\n",
    "\n",
    "if uploaded_file is not None:\n",
    "    df = wrangle(uploaded_file)\n",
    "    st.write(\"Data loaded successfully!\")\n",
    "\n",
    "    # Scatter mapbox plot\n",
    "    st.subheader(\"Scatter Mapbox Plot\")\n",
    "    fig = px.scatter_mapbox(\n",
    "        df, \n",
    "        lat=\"lat\",\n",
    "        lon=\"lon\",\n",
    "        width=600, \n",
    "        height=600, \n",
    "        color=\"yield_l_sec\",\n",
    "        hover_data=[\"yield_l_sec\"],\n",
    "    )\n",
    "    fig.update_layout(mapbox_style=\"open-street-map\")\n",
    "    st.plotly_chart(fig)\n",
    "\n",
    "    # 3D scatter plot\n",
    "    st.subheader(\"3D Scatter Plot\")\n",
    "    fig = px.scatter_3d(\n",
    "        df,\n",
    "        x=\"lon\",\n",
    "        y=\"lat\",\n",
    "        z=\"yield_l_sec\",\n",
    "        labels={\"lon\": \"longitude\", \"lat\": \"latitude\", \"yield_l_sec\": \"Discharge Rate\"},\n",
    "        width=600,\n",
    "        height=500,\n",
    "    )\n",
    "    fig.update_traces(\n",
    "        marker={\"size\": 4, \"line\": {\"width\": 2, \"color\": \"DarkSlateGrey\"}},\n",
    "        selector={\"mode\": \"markers\"},\n",
    "    )\n",
    "    st.plotly_chart(fig)\n",
    "\n",
    "    # Model training\n",
    "    target = \"yield_l_sec\"\n",
    "    features = [\"lat\", \"lon\", \"swl\", \"bh_depth\", \"curve_type\"]\n",
    "    X_train = df[features]\n",
    "    y_train = df[target]\n",
    "\n",
    "    y_mean = y_train.mean()\n",
    "    y_pred_training = [y_mean] * len(y_train)\n",
    "    mae_baseline = mean_absolute_error(y_train, y_pred_training)\n",
    "    st.write(\"Mean yield:\", y_mean)\n",
    "    st.write(\"Mean absolute error:\", mae_baseline)\n",
    "\n",
    "    model = make_pipeline(OneHotEncoder(use_cat_names=True), Ridge())\n",
    "    model.fit(X_train, y_train)\n",
    "\n",
    "    y_train_pred = model.predict(X_train)\n",
    "    mae_pred = mean_absolute_error(y_train, y_train_pred)\n",
    "    st.write(\"Training MAE:\", mae_pred.round(2))\n",
    "\n",
    "    # Prediction function\n",
    "    def make_prediction(lat, lon, swl, borehole_depth, curve_type):\n",
    "        data = {\n",
    "            \"lat\": [lat],\n",
    "            \"lon\": [lon],\n",
    "            \"swl\": [swl],\n",
    "            \"bh_depth\": [borehole_depth],\n",
    "            \"curve_type\": [curve_type]\n",
    "        }\n",
    "        df = pd.DataFrame(data)\n",
    "        prediction = model.predict(df).round(2)[0]\n",
    "        return prediction\n",
    "\n",
    "    # Interactive inputs\n",
    "    st.sidebar.subheader(\"Make Predictions\")\n",
    "    lat = st.sidebar.slider(\n",
    "        \"Latitude\", float(X_train[\"lat\"].min()), float(X_train[\"lat\"].max()), float(X_train[\"lat\"].mean()))\n",
    "    lon = st.sidebar.slider(\n",
    "        \"Longitude\", float(X_train[\"lon\"].min()), float(X_train[\"lon\"].max()), float(X_train[\"lon\"].mean()))\n",
    "    swl = st.sidebar.slider(\n",
    "        \"SWL\", int(X_train[\"swl\"].min()), int(X_train[\"swl\"].max()), int(X_train[\"swl\"].mean()))\n",
    "    borehole_depth = st.sidebar.slider(\n",
    "        \"Borehole Depth\", int(X_train[\"bh_depth\"].min()), int(X_train[\"bh_depth\"].max()), int(X_train[\"bh_depth\"].mean()))\n",
    "    curve_type = st.sidebar.selectbox(\n",
    "        \"Curve Type\", sorted(X_train[\"curve_type\"].unique()))\n",
    "\n",
    "    # Display prediction\n",
    "    if st.sidebar.button(\"Predict\"):\n",
    "        prediction = make_prediction(lat, lon, swl, borehole_depth, curve_type)\n",
    "        st.sidebar.write(f\"Predicted discharge rate: {prediction} l/s\")\n",
    "else:\n",
    "    st.write(\"Please upload a CSV file to proceed.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
