import { TagsInput } from "react-tag-input-component";
import { useState } from "react";

const Tag = () => {
  const [selected, setSelected] = useState(["gardening"]);

  return (
    <div>
      <h1>Add Tags</h1>
      <pre>{JSON.stringify(selected)}</pre>
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