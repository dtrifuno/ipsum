import {Menu} from '@headlessui/react';
import {useField} from 'formik';
import * as React from 'react';

export interface DropdownItem {
  value: string;
  label: string;
}

interface DropdownMenuProps {
  items: DropdownItem[];
  placeholderText?: string;
  name: string;
  validate?: boolean;
}

const getLabelIfPresent = (
  items: DropdownItem[],
  targetValue?: string
): string | null => {
  for (const {value, label} of items) {
    if (value === targetValue) {
      return label;
    }
  }
  return null;
};

const DropdownMenu = ({
  items,
  placeholderText,
  name,
  validate = false,
}: DropdownMenuProps) => {
  const [, {value}, {setValue}] = useField(name);
  return (
    <Menu as="div" className="relative inline-block text-left rounded-none">
      <Menu.Button className="border-2 border-black focus:border-orange-500 outline-none w-44">
        <div className="pl-2 py-1 flex flex-row items-baseline justify-between">
          {getLabelIfPresent(items, value) || placeholderText}
          <svg
            className="w-4 h-4 ml-2 mr-0.5"
            aria-hidden="true"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="3"
              d="M19 9l-7 7-7-7"
            ></path>
          </svg>
        </div>
      </Menu.Button>
      <Menu.Items className="absolute right-0 z-10 mt-0 w-44 origin-top-right bg-white">
        <div className="flex flex-col border border-black">
          {items.map(item => (
            <Menu.Item key={item.value} as={React.Fragment}>
              <button
                className="pl-2 text-left hover:text-white hover:bg-orange-500 ui-active:text-white ui-active:bg-orange-500"
                type="button"
                onClick={() => setValue(item.value, validate)}
              >
                {item.label}
              </button>
            </Menu.Item>
          ))}
        </div>
      </Menu.Items>
    </Menu>
  );
};

export default DropdownMenu;
