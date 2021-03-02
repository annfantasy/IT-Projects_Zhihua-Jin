export const loginRules = {
  username: [{ validate: (val) => !!val, message: 'Username is required' },
    { validate: (val) => val.length >= 3, message: 'Username is too short' }],
  password: [{ validate: (val) => !!val, message: 'Password is required' },
    { validate: (val) => val.length >= 3 && val.length <= 18, message: 'Length of password needs to be from 3 to 18' }],
  agree: [{ validate: (val) => !!val, message: 'Please check the agreement' }]
}

export const registerRules = {
  username: [{ validate: (val) => !!val, message: 'Username is required' },
    { validate: (val) => val.length >= 3 && val.length <= 18, message: 'Length of username needs to be from 3 to 18' }],
  password: [{ validate: (val) => !!val, message: 'Password is required' },
    { validate: (val) => val.length >= 3 && val.length <= 18, message: 'Length of password needs to be from 3 to 18' }],
  name: [{ validate: (val) => !!val, message: 'Name is required' },
    { validate: (val) => val.length >= 3 && val.length <= 18, message: 'Length of name needs to be from 3 to 18' }]
}

export const postRules = {
  title: [{ validate: (val) => !!val, message: 'Title is required' },
    { validate: (val) => val.length >= 3 && val.length <= 18, message: 'Length of title needs to be from 3 to 18' }],
  content: [{ validate: (val) => !!val, message: 'Content is required' },
    { validate: (val) => val.length >= 5, message: 'Length of password needs to be greater than 5' }],
  adminPassword: [{ validate: (val) => !!val, message: 'Content is required' },
    { validate: (val) => val === 'admin', message: 'Admin password is wrong.' }]
}

export const editProfileRules = {
  name: [{ validate: (val) => !!val, message: 'Name is required' },
    { validate: (val) => val.length >= 3, message: 'Name is too short' }]
}

export function isvalidUsername(str) {
  const valid_map = ['admin', 'editor']
  return valid_map.indexOf(str.trim()) >= 0
}

export function isExternal(path) {
  return /^(https?:|mailto:|tel:)/.test(path)
}
