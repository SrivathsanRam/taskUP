/* eslint-disable react/prop-types */
import { TagsInput } from "react-tag-input-component";
//import { useState } from "react";

const Tag = ({selected, setSelected}) => {
  //const [selected, setSelected] = useState(["gardening","cleaning","pick-up","share food"]);

  return (
    <div>
      <TagsInput
        value={selected}
        onChange={setSelected}
        name="tasks"
        placeHolder="enter tags"
      />
      <em>press enter to add new tag</em>
    </div>
  );
};

export default Tag;