# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
from streamlit_elements import elements, mui, html

LOGGER = get_logger(__name__)


def run():
  st.set_page_config(
      layout="wide",
      initial_sidebar_state="collapsed",
      page_title="Hello",
      page_icon="👋",
  )
  
  with elements("dashboard"):
    from streamlit_elements import dashboard
    
    
    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 4, 3),
        dashboard.Item("second_item", 4, 0, 4, 3),
        dashboard.Item("third_item", 4, 4, 4, 3),
        dashboard.Item("fourth_item", 0, 8, 4, 3),
        dashboard.Item("fifth_item", 8, 0, 4, 6),
    ]
    
    
    # If you want to retrieve updated layout values as the user move or resize dashboard items,
    # you can pass a callback to the onLayoutChange event parameter.

    def handle_layout_change(updated_layout): ##!I could save this to local storage or something
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)
        
        

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        mui.Paper("Do It", key="first_item", sx={"bgcolor": "#B3FFB3", "alignContent":"center"}) ##?onDoubleClick to create a new paper? maybe button
        mui.Paper("Plan It", key="second_item", sx={"bgcolor": "#FBFFB3",})
        mui.Paper("Delegate It", key="third_item", sx={"bgcolor": "#B3F6FF",})
        mui.Paper("Drop It", key="fourth_item", sx={"bgcolor": "#FFB9B3",})
        mui.Paper("Done It", key="fifth_item", sx={"bgcolor": "#B3FFB3",})
  


if __name__ == "__main__":
    run()
