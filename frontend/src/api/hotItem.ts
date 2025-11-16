import request from "./request";

export const getHotItems = (source?: string) => {
  return request.get("hot/", {
    params: {
      source: source,
    },
  });
};
